# -*- coding: utf-8 -*-
from django.conf.urls.defaults import *

urlpatterns = patterns("ircquotes.quotes.views",
	(r"^(?P<channel>\w+)/$", "list_quotes"),
)
