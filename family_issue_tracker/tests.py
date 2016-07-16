from django.test import TestCase, Client
from django.core.urlresolvers import reverse

from issues.models import Issue, Comment, SandstormUser

from datetime import date, timedelta

class IssuesTests(TestCase):
    def setUp(self):
        u = SandstormUser(sid="xxxdummyxxx", name="Dummy User", handle="dummy")
        u.save()

        i1 = Issue(title="Foo", description="describe Foo", creator=u, deadline=date.today())
        i1.save()
        i2 = Issue(title="Bar", description="describe Bar", for_anon=True, creator=u, deadline=date.today() + timedelta(days=2))
        i2.save()
        i3 = Issue(title="Baz", description="describe Baz", subscriber_only=True, creator=u)
        i3.save()

        c1_1 = Comment(body="Hohoho", issue=i1, creator=u)
        c1_1.save()
        c2_1 = Comment(body="Funny!", issue=i1, creator=u)
        c2_1.save()

    def test_setup_state(self):
        """Does not change state"""
        c = Client()
        # index
        with self.assertNumQueries(5): # TODO should be less
            r = c.get("/", follow=True)
        self.assertEqual(r.status_code, 200)
        assert "<html" in r.content.decode("utf8")
        assert len(r.context['issues']) == 3

        # specific issue
        with self.assertNumQueries(3):
            r = c.get("/i/1")
        self.assertEquals(r.status_code, 200)
        assert "<html" in r.content.decode("utf8")
        issue = r.context['issue']
        self.assertEqual(issue.id, 1)
        self.assertEqual(issue.title, "Foo")
        comments = r.context['issue'].comments.all()
        self.assertEqual(len(comments), 2)

        # specific issue edit page
        with self.assertNumQueries(3):
            r = c.get("/i/1/edit")
        self.assertEquals(r.status_code, 200)
        assert "<html" in r.content.decode("utf8")

        # specific user
        with self.assertNumQueries(3):
            r = c.get(reverse("show_user", args=["anonym"]))
        self.assertEquals(r.status_code, 200)
        assert "<html" in r.content.decode("utf8")

    def test_creation(self):
        """Adding an issue and a comment"""
        c = Client()
        with self.assertNumQueries(3):
            r = c.get(reverse("create_issue"))
        self.assertEqual(r.status_code, 200)
        assert "<form" in r.content.decode("utf8")

        self.assertEqual(len(Issue.objects.all()), 3)
        with self.assertNumQueries(5): # TODO should be less
            r = c.post("/i/create", dict(title="My Issue", description="Yeah"), follow=True)
        self.assertEqual(r.status_code, 200)
        self.assertEqual(len(Issue.objects.all()), 4)
        issue = r.context['issue']
        self.assertEqual(issue.id, 4)
        self.assertEqual(issue.title, "My Issue")
        comments = r.context['issue'].comments.all()
        self.assertEqual(len(comments), 0)

        self.assertEqual(len(Comment.objects.all()), 2)
        with self.assertNumQueries(4):
            r = c.post("/i/create_comment", dict(body="My Comment", issue=issue.id))
        self.assertEqual(r.status_code, 302)
        self.assertEqual(len(Comment.objects.all()), 3)

        with self.assertNumQueries(3):
            r = c.get(r.url)
        self.assertEqual(r.status_code, 200)
        comments = r.context['issue'].comments.all()
        self.assertEqual(len(comments), 1)

    def test_close_reopen(self):
        """Close and reopen an issue"""
        c = Client()
        with self.assertNumQueries(4): # TODO should be less
            r = c.post(reverse("close_issue"), dict(issue_id=1))
        self.assertEqual(r.status_code, 302)
        i1 = Issue.objects.get(pk=1)
        self.assertNotEqual(i1.closed, None)

        with self.assertNumQueries(3): # TODO should be less
            r = c.post(reverse("reopen_issue"), dict(issue_id=1))
        self.assertEqual(r.status_code, 302)
        i1 = Issue.objects.get(pk=1)
        self.assertEqual(i1.closed, None)
