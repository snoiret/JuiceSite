# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-14 07:38
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0043_auto_20170808_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 21, 7, 38, 29, 203499, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 21, 7, 38, 29, 205777, tzinfo=utc)),
        ),
    ]
