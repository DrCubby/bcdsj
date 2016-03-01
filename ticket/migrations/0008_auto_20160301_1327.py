# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-01 13:27
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0007_auto_20160226_1215'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feature',
            name='date_created',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='feature',
            name='date_target',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='feature',
            name='priority',
            field=models.IntegerField(default=1),
        ),
    ]
