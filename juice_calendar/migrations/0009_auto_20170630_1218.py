# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-30 12:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0008_auto_20170630_1129'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 7, 12, 18, 20, 437018, tzinfo=utc)),
        ),
    ]
