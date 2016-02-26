# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-26 15:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField()),
                ('file', models.FileField(upload_to='uploads/%Y/%m')),
                ('capture_date', models.DateTimeField()),
                ('capture_location', models.CharField(max_length=200)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
