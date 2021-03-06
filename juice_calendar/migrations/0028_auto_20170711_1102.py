# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-11 11:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0027_auto_20170711_0544'),
    ]

    operations = [
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 18, 11, 2, 38, 46978, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='productitem',
            name='sub_system',
            field=models.ManyToManyField(blank=True, to='juice_calendar.ProductItem'),
        ),
    ]
