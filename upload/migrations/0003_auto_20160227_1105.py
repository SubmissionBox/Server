# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-27 11:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('upload', '0002_auto_20160226_1552'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='capture_date',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='upload',
            name='capture_location',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='upload',
            name='torchat_id',
            field=models.CharField(blank=True, max_length=16),
        ),
    ]