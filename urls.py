# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns("",
	(r"^admin/doc/", include("django.contrib.admindocs.urls")),
	(r"^admin/", include(admin.site.urls)),
	(r"^static/(?P<path>.*)$", "django.views.static.serve", {"document_root": "/home/adys/src/git/ircquotes/static"}),
	(r"^", include("ircquotes.quotes.urls")),
)
