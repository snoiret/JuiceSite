# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-06-28 13:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0002_auto_20170628_1318'),
    ]

    operations = [
        migrations.AddField(
            model_name='productitem',
            name='name',
            field=models.CharField(default='Unnamed', max_length=200),
        ),
    ]
