from django.conf.urls import patterns, url

from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^(?P<id>[0-9]+)$', show, name='show_issue'),
    url(r'^create^$', create, name='create_issue'),
]
