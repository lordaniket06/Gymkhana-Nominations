# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-23 22:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0083_groupnomination_approvals'),
    ]

    operations = [
        migrations.AddField(
            model_name='groupnomination',
            name='creator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='nomi.Post'),
        ),
    ]
