# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-16 08:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('tieba', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 8, 16, 8, 39, 13, 150739, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
