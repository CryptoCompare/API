# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-30 05:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coinbasehistory',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='coinhakohistory',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='zebpayhistory',
            name='timestamp',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]