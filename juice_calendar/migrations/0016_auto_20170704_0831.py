# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-04 08:31
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0015_auto_20170704_0623'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 11, 8, 31, 12, 818182, tzinfo=utc)),
        ),
    ]
