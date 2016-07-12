from django.db import models

class Issue(models.Model):
    title = models.CharField(max_length=60)
    description = models.TextField(
        help_text="Editable text field")
    created = models.DateTimeField(auto_now_add=True)
    closed = models.DateTimeField(null=True, blank=True)
    for_anon = models.BooleanField(default=False,
        help_text="Anonymous users can see this issue")
    subscriber_only = models.BooleanField(default=False,
        help_text="Only subscribers see this issue")

    def __unicode__(self):
        return self.title

class Comment(models.Model):
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE,
        related_name="comments")
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
