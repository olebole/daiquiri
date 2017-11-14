# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-14 14:49
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Record',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('resource_type', models.CharField(max_length=32)),
                ('resource', jsonfield.fields.JSONField()),
                ('client_ip', models.GenericIPAddressField(blank=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-time',),
                'verbose_name': 'Record',
                'verbose_name_plural': 'Records',
                'permissions': (('view_record', 'Can view Record'),),
            },
        ),
    ]
