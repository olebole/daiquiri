# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-04-13 11:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daiquiri_metadata', '0021_table_nrows'),
    ]

    operations = [
        migrations.AddField(
            model_name='table',
            name='size',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Size of the table in bytes'),
        ),
    ]