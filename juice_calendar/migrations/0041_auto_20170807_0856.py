# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-07 06:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0040_auto_20170807_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 14, 6, 56, 12, 50009, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 14, 6, 56, 12, 52310, tzinfo=utc)),
        ),
    ]
