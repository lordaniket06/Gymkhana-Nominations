# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-08-30 12:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0150_auto_20170822_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='nominationinstance',
            name='submission_status',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='nominationinstance',
            name='timestamp',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
