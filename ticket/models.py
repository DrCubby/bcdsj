from __future__ import unicode_literals


from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Feature(models.Model):
    title = models.CharField(max_length=200)
    client = models.ForeignKey(Client, default=0, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, default=0, on_delete=models.CASCADE)
    priority = models.IntegerField(blank=False,default=0,null=False)
    description = models.TextField()
    url = models.URLField(blank=True)
    date_created = models.DateTimeField(default=timezone.now)
    date_target = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.title





