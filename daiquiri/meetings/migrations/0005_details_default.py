# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-01 12:00
from __future__ import unicode_literals

from django.db import migrations
import jsonfield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('daiquiri_meetings', '0004_blank_contribution_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='participant',
            name='details',
            field=jsonfield.fields.JSONField(blank=True, default={}, help_text='Choices are given by settings.MEETINGS_PARTICIPANT_DETAIL_KEYS', null=True, verbose_name='Details'),
        ),
    ]