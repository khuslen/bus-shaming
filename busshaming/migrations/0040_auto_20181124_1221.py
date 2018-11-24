# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-11-24 12:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busshaming', '0039_auto_20181124_1219'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tripdate',
            name='schedule_relationship',
            field=models.SmallIntegerField(blank=True, choices=[(1, 'SCHEDULED'), (2, 'ADDED'), (3, 'UNSCHEDULED'), (4, 'CANCELLED')], null=True),
        ),
    ]