# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-08-01 06:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0038_auto_20170731_1008'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 8, 6, 12, 13, 938389, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 8, 8, 6, 12, 13, 939655, tzinfo=utc)),
        ),
    ]