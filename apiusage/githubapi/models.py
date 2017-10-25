# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from datetime import datetime 
from django.db import models
# Create your models here.
 
class SearchUsers(models.Model):
	login = models.CharField(max_length=20)
	url = models.URLField()
	created_at = models.DateTimeField(default=datetime.now, blank=True)
	avatar_url = models.URLField()
	