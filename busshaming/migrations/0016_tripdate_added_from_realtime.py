# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-12-31 23:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busshaming', '0015_feed_last_processed_dump'),
    ]

    operations = [
        migrations.AddField(
            model_name='tripdate',
            name='added_from_realtime',
            field=models.BooleanField(default=False),
        ),
    ]
