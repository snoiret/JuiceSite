# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-13 07:05
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0031_auto_20170713_0629'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='phase',
            field=models.CharField(choices=[('ITT', 'ITT Phase'), ('DEV', 'DevelopmentPhase'), ('H/W', 'H/W Phase'), ('QUA', 'Quality Review')], default='ITT', max_length=3),
        ),
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 20, 7, 5, 26, 547566, tzinfo=utc)),
        ),
    ]