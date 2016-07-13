from datetime import datetime

from django.db import models
from django.utils.translation import ugettext_lazy as _

class Issue(models.Model):
    title = models.CharField(max_length=60,
        verbose_name=_("title"))
    description = models.TextField(null=True, blank=True,
        verbose_name=_("description"),
        help_text="Editable text field")
    creator = models.CharField(max_length=256, blank=True,
        verbose_name=_("creator"))
    created = models.DateTimeField(auto_now_add=True,
        verbose_name=_("created"))
    closed = models.DateTimeField(null=True, blank=True,
        verbose_name=_("closed"))
    for_anon = models.BooleanField(default=False,
        verbose_name=_("for anonymous"),
        help_text="Anonymous users can see this issue")
    subscriber_only = models.BooleanField(default=False,
        verbose_name=_("subscriber only"),
        help_text="Only subscribers see this issue")

    def __unicode__(self):
        return self.title

    def close(self):
        self.closed = datetime.now()
        self.save()

    def reopen(self):
        self.closed = None
        self.save()

class Comment(models.Model):
    issue = models.ForeignKey('Issue', on_delete=models.CASCADE,
        verbose_name=_("issue"),
        related_name="comments")
    body = models.TextField(
        verbose_name=_("text body"))
    creator = models.CharField(max_length=256, blank=True,
        verbose_name=_("creator"))
    created = models.DateTimeField(auto_now_add=True,
        verbose_name=_("created"))
