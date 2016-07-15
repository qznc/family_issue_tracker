from datetime import datetime, date, timedelta

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Issue(models.Model):
    title = models.CharField(max_length=60,
        verbose_name=_("title"))
    description = models.TextField(null=True, blank=True,
        verbose_name=_("description"),
        help_text="Editable text field")
    creator = models.ForeignKey('SandstormUser',
        verbose_name=_("creator"))
    created = models.DateTimeField(auto_now_add=True,
        verbose_name=_("created"))
    deadline = models.DateField(null=True, blank=True,
        verbose_name=_("deadline"))
    closed = models.DateTimeField(null=True, blank=True,
        verbose_name=_("closed"))
    for_anon = models.BooleanField(default=False,
        verbose_name=_("for anonymous"),
        help_text="Anonymous users can see this issue")
    subscriber_only = models.BooleanField(default=False,
        verbose_name=_("subscriber only"),
        help_text="Only subscribers see this issue")
    responsible = models.ForeignKey('SandstormUser', null=True, blank=True,
        related_name="working_on", verbose_name=_("responsible"))

    def __str__(self):
        return self.title

    def close(self):
        self.closed = datetime.now()
        self.save()

    def reopen(self):
        self.closed = None
        self.save()

    def deadline_css_classes(self):
        dead = self.deadline
        if not dead:
            return ""
        today = date.today()
        print(today, "vs", dead)
        if dead == today:
            return "today"
        if dead < today:
            return "missed"
        if dead < today + timedelta(days=7):
            return "within_week"
        return ""

    def allComments(self):
        return Comment.objects.select_related('creator').filter(issue=self).all()

class Comment(models.Model):
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE,
        verbose_name=_("issue"),
        related_name="comments")
    body = models.TextField(
        verbose_name=_("text body"))
    creator = models.ForeignKey('SandstormUser', null=True, blank=True,
        verbose_name=_("creator"))
    created = models.DateTimeField(auto_now_add=True,
        verbose_name=_("created"))

class SandstormUser(models.Model):
    sid = models.CharField(max_length=32, primary_key=True, default="anon")
    name = models.CharField(max_length=1024)
    handle = models.CharField(max_length=1024, null=True, blank=True)
    gender = models.CharField(max_length=64)
    image_url = models.CharField(max_length=1024, null=True, blank=True)

    def __str__(self):
        return self.name
