# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-29 01:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0008_auto_20160329_0119'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='face_size',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
    ]
