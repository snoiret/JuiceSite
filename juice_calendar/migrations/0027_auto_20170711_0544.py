# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-11 05:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0026_auto_20170710_1241'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 18, 5, 44, 54, 189076, tzinfo=utc)),
        ),
    ]
