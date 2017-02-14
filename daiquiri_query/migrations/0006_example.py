# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-02-14 13:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
        ('daiquiri_query', '0005_meta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True, null=True)),
                ('query_string', models.TextField()),
                ('groups', models.ManyToManyField(blank=True, to='auth.Group')),
            ],
            options={
                'ordering': ('order',),
                'verbose_name': 'Example',
                'verbose_name_plural': 'Examples',
                'permissions': (('view_example', 'Can view Example'),),
            },
        ),
    ]
