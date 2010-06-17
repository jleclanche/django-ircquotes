# -*- coding: utf-8 -*-

from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from quotes.models import Quote
from django.utils.html import escape

import re

def markup_timestamp(ts):
	ts_text = ts.group(1)
	return "<tt>[%s]</tt>" % (ts_text)

def markup(text):
	res = text.strip()
	res = escape(res)
	res = re.sub(r"((?:\[.*?\])\s*)(\*{3} [^\s]+) \(.+?\)", r"\1\2", res)
	res = re.sub(r"((?:\[.*?\])\s*)\*{4} ([^\s]+ \(.+?\))", r"\1* \2", res)
	res = re.sub(r"(?m)^((?:\[[\d\.:]*?\]\s*)?)(\* .*?)\s*$", r'\1<span class="action">\2</span>', res)
	res = re.sub(r"(?m)^((?:\[[\d\.:]*?\]\s*)?)(\*\*\* .*?)\s*$", r'\1<span class="system">\2</span>', res)
	res = re.sub(r"(?m)^((?:\[[\d\.:]*?\])\s*)(-.*?- .+)\s*$", r'\1<span class="privmsg">\2</span>', res)
	res = re.sub(r"(?m)^\[(.*?)\]", markup_timestamp, res)
	res = re.sub(r"(?i)(\b([^\s;]+)://[-A-Z0-9+&@#/%?=~_|!:,.;]*[-A-Z0-9+@#/%=~_|])", r'<a href="\1">\1</a>', res)
	res = re.sub(r"  ", r"&nbsp;&nbsp;", res)
	res = re.sub(r"\r?\n", r"<br />\n", res)
	return unicode(res)

def list_quotes(request, channel):
	channel = channel.lower()
	quotes = Quote.objects.filter(channel=channel)
	if not quotes:
		raise Http404
	return render_to_response("quotes/listing.html", {"quotes": quotes, "channel": channel})

