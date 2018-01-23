# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-01-23 11:03
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import jsonfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contribution',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256, verbose_name='Title')),
                ('abstract', models.TextField(blank=True, null=True, verbose_name='Abstract')),
                ('contribution_type', models.CharField(help_text='Choices are given by settings.MEETINGS_CONTRIBUTION_TYPES', max_length=8, verbose_name='Contribution type')),
                ('accepted', models.BooleanField(default=False, help_text='Designates whether the contribution is accepted.', verbose_name='Accepted')),
            ],
            options={
                'ordering': ('participant', 'title'),
                'verbose_name': 'Contribution',
                'verbose_name_plural': 'Contributions',
                'permissions': (('view_contribution', 'Can view Contribution'),),
            },
        ),
        migrations.CreateModel(
            name='Meeting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Title of the meeting', max_length=256, verbose_name='Title')),
                ('slug', models.SlugField(help_text='Slug for the URL of the meeting', max_length=256, verbose_name='Slug')),
                ('registration_message', models.TextField(blank=True, help_text='Message on registration page', null=True, verbose_name='Registration message')),
                ('participants_message', models.TextField(blank=True, help_text='Message on participants page', null=True, verbose_name='Participants message')),
                ('contributions_message', models.TextField(blank=True, help_text='Message on contributions page', null=True, verbose_name='Contributions message')),
                ('registration_open', models.BooleanField(default=False, help_text='Designates whether the registration page is publicly accessible.', verbose_name='Registration open')),
                ('participants_open', models.BooleanField(default=False, help_text='Designates whether the participants page is publicly accessible.', verbose_name='Participants list open')),
                ('contributions_open', models.BooleanField(default=False, help_text='Designates whether the contributions page is publicly accessible.', verbose_name='Contributions list open')),
            ],
            options={
                'ordering': ('title',),
                'verbose_name': 'Meeting',
                'verbose_name_plural': 'Meetings',
                'permissions': (('view_meeting', 'Can view Meeting'),),
            },
        ),
        migrations.CreateModel(
            name='Participant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=256, verbose_name='First name')),
                ('last_name', models.CharField(max_length=256, verbose_name='Last name')),
                ('email', models.EmailField(max_length=256, verbose_name='Email')),
                ('details', jsonfield.fields.JSONField(blank=True, help_text='Choices are given by settings.MEETINGS_PARTICIPANT_DETAIL_KEYS', null=True, verbose_name='Details')),
                ('registered_on', models.DateTimeField(help_text='Datetime this participant has submitted his/her registration', verbose_name='Registered on')),
                ('accepted', models.BooleanField(default=False, help_text='Designates whether the participant is accepted.', verbose_name='Accepted')),
                ('meeting', models.ForeignKey(help_text='Meeting this participant has registered for', on_delete=django.db.models.deletion.CASCADE, related_name='participants', to='daiquiri_meetings.Meeting', verbose_name='Meeting')),
            ],
            options={
                'ordering': ('meeting', 'last_name', 'first_name'),
                'verbose_name': 'Participant',
                'verbose_name_plural': 'Participants',
                'permissions': (('view_participant', 'Can view Participant'),),
            },
        ),
        migrations.AddField(
            model_name='contribution',
            name='participant',
            field=models.ForeignKey(help_text='Participant who submitted this contribution', on_delete=django.db.models.deletion.CASCADE, related_name='contributions', to='daiquiri_meetings.Participant', verbose_name='Participant'),
        ),
    ]
