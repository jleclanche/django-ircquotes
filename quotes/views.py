# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from quotes.models import Quote

def list_quotes(request, channel):
	channel = channel.lower()
	quotes = Quote.objects.filter(channel=channel)
	if not quotes:
		raise Http404
	return render_to_response("quotes/listing.html", {"quotes": quotes, "channel": channel})

