# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-19 12:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0004_auto_20170819_1909'),
    ]

    operations = [
        migrations.AddField(
            model_name='bitcoinlivedata',
            name='lastDayMax',
            field=models.DecimalField(decimal_places=10, default=-1, max_digits=20),
        ),
        migrations.AddField(
            model_name='bitcoinlivedata',
            name='lastDayMin',
            field=models.DecimalField(decimal_places=10, default=-1, max_digits=20),
        ),
        migrations.AddField(
            model_name='bitcoinlivedata',
            name='lastHourMax',
            field=models.DecimalField(decimal_places=10, default=-1, max_digits=20),
        ),
        migrations.AddField(
            model_name='bitcoinlivedata',
            name='lastHourMin',
            field=models.DecimalField(decimal_places=10, default=-1, max_digits=20),
        ),
        migrations.AddField(
            model_name='bitcoinlivedata',
            name='lastMonthMax',
            field=models.DecimalField(decimal_places=10, default=-1, max_digits=20),
        ),
        migrations.AddField(
            model_name='bitcoinlivedata',
            name='lastMonthMin',
            field=models.DecimalField(decimal_places=10, default=-1, max_digits=20),
        ),
        migrations.AddField(
            model_name='bitcoinlivedata',
            name='lastWeekMax',
            field=models.DecimalField(decimal_places=10, default=-1, max_digits=20),
        ),
        migrations.AddField(
            model_name='bitcoinlivedata',
            name='lastWeekMin',
            field=models.DecimalField(decimal_places=10, default=-1, max_digits=20),
        ),
    ]
