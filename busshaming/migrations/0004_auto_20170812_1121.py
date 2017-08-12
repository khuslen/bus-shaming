# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-12 11:21
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('busshaming', '0003_feed_slug'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agency',
            old_name='feed_id',
            new_name='feed',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='agency_id',
            new_name='agency',
        ),
        migrations.RenameField(
            model_name='route',
            old_name='feed_id',
            new_name='feed',
        ),
        migrations.RenameField(
            model_name='trip',
            old_name='route_id',
            new_name='route',
        ),
        migrations.RenameField(
            model_name='tripstop',
            old_name='stop_id',
            new_name='stop',
        ),
        migrations.RenameField(
            model_name='tripstop',
            old_name='trip_id',
            new_name='trip',
        ),
        migrations.RenameField(
            model_name='triptimetable',
            old_name='trip_id',
            new_name='trip',
        ),
        migrations.AlterUniqueTogether(
            name='agency',
            unique_together=set([('gtfs_agency_id', 'feed')]),
        ),
        migrations.AlterUniqueTogether(
            name='route',
            unique_together=set([('gtfs_route_id', 'feed')]),
        ),
        migrations.AlterUniqueTogether(
            name='trip',
            unique_together=set([('gtfs_trip_id', 'version', 'route')]),
        ),
        migrations.AlterUniqueTogether(
            name='tripstop',
            unique_together=set([('trip', 'stop')]),
        ),
    ]