# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 02:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0005_feature_client'),
    ]

    operations = [
        migrations.AddField(
            model_name='feature',
            name='url',
            field=models.URLField(blank=True),
        ),
    ]
