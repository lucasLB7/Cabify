# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-06-26 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('driver', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='driver',
            name='national_id',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='driver',
            name='phone_number',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]