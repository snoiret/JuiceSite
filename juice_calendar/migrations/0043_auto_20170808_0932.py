# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-08 07:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0042_auto_20170808_0819'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 7, 32, 49, 481137, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 15, 7, 32, 49, 483453, tzinfo=utc)),
        ),
    ]
