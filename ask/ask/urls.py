
from django.conf.urls import patterns, include, url

from django.contrib import admin

from qa.views import question, index, login, signup, ask, popular, new

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', index),
    url(r'^login/$', login),
    url(r'^signup/$', signup),
    url(r'^question/\d+/$', question),
    url(r'^ask/.*$', ask),
    url(r'^popular/$', popular),
    url(r'^new/$', new),
)