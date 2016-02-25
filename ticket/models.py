from __future__ import unicode_literals

from django.db import models
from django.utils import timezone

class Feature(models.Model):
    author = models.ForeignKey('auth.User')
    client = models.ForeignKey('Client')
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_target = models.DateTimeField(blank=True, null=True)

class Client(models.Model):
    name = models.CharField(max_length=200)

