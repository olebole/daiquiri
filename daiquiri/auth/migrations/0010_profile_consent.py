# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-15 15:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('daiquiri_auth', '0009_delete_detailkey'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='consent',
            field=models.BooleanField(default=False, help_text='Designates whether the user has agreed to the terms of use.', verbose_name='Consent'),
        ),
    ]