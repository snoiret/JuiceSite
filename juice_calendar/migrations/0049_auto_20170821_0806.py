# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-21 06:06
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0048_auto_20170818_0824'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 28, 6, 6, 59, 161020, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 28, 6, 6, 59, 163283, tzinfo=utc)),
        ),
    ]
