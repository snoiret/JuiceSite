# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-24 07:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0035_auto_20170721_0804'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 31, 7, 37, 9, 483876, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 31, 7, 37, 9, 485169, tzinfo=utc)),
        ),
    ]
