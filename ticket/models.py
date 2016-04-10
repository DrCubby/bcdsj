from __future__ import unicode_literals


from django.db import models
from django.utils import timezone

class Sale(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Status(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Item(models.Model):

    Unsold = 'Unsold'
    Grays = 'Grays'
    Ebay = 'Ebay'

    sale_place_choices = (
        (Unsold, 'Unsold'),
        (Grays, 'Grays'),
        (Ebay, 'Ebay'),
    )

    title = models.CharField(max_length=50)
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    purchase_number = models.CharField(max_length=50, null=True, blank=True)
    #priority = models.IntegerField(blank=False,default=1,null=False)
    #description = models.TextField()
    #date_target = models.DateField(blank=True, null=True)
    #url = models.URLField(blank=True)
    #date_created = models.DateField(default=timezone.now)
    image = models.ImageField(upload_to = 'img', null=True, blank=True)
    purchase_price = models.CharField(max_length=50, null=True, blank=True)
    sold_price = models.IntegerField(blank=False, default=0, null=False)
    sale_place = models.CharField(max_length=50, choices=sale_place_choices, default=Unsold)
    metal = models.CharField(max_length=50, null=True, blank=True)
    carat = models.CharField(max_length=50, null=True, blank=True)
    date_bought = models.DateField(blank=True, null=True)
    date_sold = models.DateField(blank=True, null=True)
    weight = models.CharField(max_length=50, null=True, blank=True)
    size = models.CharField(max_length=50, null=True, blank=True)
    stone = models.CharField(max_length=50, null=True, blank=True)
    notes = models.CharField(max_length=250, null=True, blank=True)
    face_size = models.IntegerField(blank=True, default=0, null=True)



    def __str__(self):
        return self.title
