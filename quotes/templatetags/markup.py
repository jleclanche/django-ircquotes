# -*- coding: utf-8 -*-
import re
from django import template
from django.utils.html import escape

register = template.Library()

@register.filter
def markup(text):
	res = text.strip()
	res = escape(res)
	res = re.sub(r"((?:\[.*?\])\s*)(\*{3} [^\s]+) \(.+?\)", r"\1\2", res)
	res = re.sub(r"((?:\[.*?\])\s*)\*{4} ([^\s]+ \(.+?\))", r"\1* \2", res)
	res = re.sub(r"(?m)^((?:\[[\d\.:]*?\]\s*)?)(\* .*?)\s*$", r'\1<span class="action">\2</span>', res)
	res = re.sub(r"(?m)^((?:\[[\d\.:]*?\]\s*)?)(\*\*\* .*?)\s*$", r'\1<span class="system">\2</span>', res)
	res = re.sub(r"(?m)^((?:\[[\d\.:]*?\])\s*)(-.*?- .+)\s*$", r'\1<span class="privmsg">\2</span>', res)
	res = re.sub(r"(?m)^\[(.*?)\]", r"<tt>[\1]</tt>", res)
	res = re.sub(r"(?i)(\b([^\s;]+)://[-A-Z0-9+&@#/%?=~_|!:,.;]*[-A-Z0-9+@#/%=~_|])", r'<a href="\1">\1</a>', res)
	res = re.sub(r"  ", r"&nbsp;&nbsp;", res)
	res = re.sub(r"\r?\n", r"<br/>\n", res)
	return unicode(res)
