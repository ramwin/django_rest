# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-31 03:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tieba', '0002_remove_album_artist'),
    ]

    operations = [
        migrations.AddField(
            model_name='test',
            name='text',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
