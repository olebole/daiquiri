# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-25 11:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('daiquiri_metadata', '0008_refactoring'),
    ]

    operations = [
        migrations.RenameField(
            model_name='column',
            old_name='size',
            new_name='arraysize',
        ),
    ]
