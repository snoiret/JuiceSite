# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-10 12:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0025_auto_20170710_1224'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 17, 12, 41, 52, 579253, tzinfo=utc)),
        ),
    ]
