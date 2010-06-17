# -*- coding: utf-8 -*-
from django.db.models import *

class Quote(Model):
	text = TextField()
	channel = CharField(max_length=16)
	date = DateTimeField(auto_now=True)

