from django.conf.urls import patterns, url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<id>[0-9]+)$', show, name='show_issue'),
    url(r'^u/(?P<id>[a-z0-9]+)$', show_user, name='show_user'),
    url(r'^(?P<id>[0-9]+)/edit$', edit, name='edit_issue'),
    url(r'^create$', create, name='create_issue'),
    url(r'^create_comment$', create_comment, name='create_comment'),
    url(r'^close_issue$', close_issue, name='close_issue'),
    url(r'^reopen_issue$', reopen_issue, name='reopen_issue'),
]
