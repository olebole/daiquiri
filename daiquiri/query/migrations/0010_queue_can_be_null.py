# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-12 10:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daiquiri_query', '0009_remove_choices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='queryjob',
            name='queue',
            field=models.CharField(blank=True, max_length=16, null=True),
        ),
    ]