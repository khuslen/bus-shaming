# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-13 04:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busshaming', '0006_auto_20170812_2338'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripstop',
            name='arrival_time',
            field=models.CharField(max_length=8),
        ),
        migrations.AlterField(
            model_name='tripstop',
            name='departure_time',
            field=models.CharField(max_length=8),
        ),
    ]