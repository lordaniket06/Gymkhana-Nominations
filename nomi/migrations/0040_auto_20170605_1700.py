# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-06-05 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nomi', '0039_auto_20170605_1418'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='nominationchoice',
            name='dept_choice',
        ),
        migrations.RemoveField(
            model_name='nominationchoice',
            name='hall_choice',
        ),
        migrations.RemoveField(
            model_name='nominationchoice',
            name='year_choice',
        ),
        migrations.AddField(
            model_name='nomination',
            name='dept_choice',
            field=models.CharField(choices=[('All', 'All'), ('Aerospace Engineering', 'AE'), ('Biological Sciences & Engineering', 'BSBE'), ('Chemical Engineering', 'CHE'), ('Civil Engineering', 'CE'), ('Computer Science & Engineering', 'CSE'), ('Electrical Engineering', 'EE'), ('Materials Science & Engineering', 'MSE'), ('Mechanical Engineering', 'ME'), ('Industrial & Management Engineering', 'IME'), ('Chemistry', 'CHM'), ('Mathematics & Scientific Computing', 'MTH'), ('Physics', 'PHY'), ('Earth Sciences', 'ES')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='nomination',
            name='hall_choice',
            field=models.CharField(choices=[(0, 'All'), (1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10'), (11, '11'), (12, '12')], max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='nomination',
            name='year_choice',
            field=models.CharField(choices=[('All', 'All'), ('Y16', 'Y16'), ('Y15', 'Y15'), ('Y14', 'Y14'), ('Y13', 'Y13'), ('Y12', 'Y12'), ('Y11', 'Y11')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='NominationChoice',
        ),
    ]