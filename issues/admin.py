from django.contrib import admin
from .models import Issue, Comment

class IssueAdmin(admin.ModelAdmin):
	list_display = ('title', 'created', 'closed', 'for_anon', 'subscriber_only')

class CommentAdmin(admin.ModelAdmin):
	list_display = ('pk', 'issue', 'created')

admin.site.register(Issue, IssueAdmin)
admin.site.register(Comment, CommentAdmin)

