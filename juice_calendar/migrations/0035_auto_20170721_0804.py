# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-07-21 08:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('juice_calendar', '0034_auto_20170719_1311'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('task_name', models.CharField(default='Unnamed', max_length=200)),
                ('due_date', models.DateTimeField(default=datetime.datetime(2017, 7, 28, 8, 4, 36, 657879, tzinfo=utc))),
                ('description', models.TextField(null=True)),
                ('product_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='juice_calendar.ProductItem')),
            ],
        ),
        migrations.AlterField(
            model_name='occurence',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2017, 7, 28, 8, 4, 36, 656646, tzinfo=utc)),
        ),
    ]