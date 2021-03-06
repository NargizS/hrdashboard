# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-05-03 15:46
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_auto_20180503_2143'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='city',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='experience',
            field=models.CharField(default=1, max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gender',
            field=models.TextField(blank=True, max_length=500),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gpa',
            field=models.CharField(default=django.utils.timezone.now, max_length=4),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='userprofile',
            name='university',
            field=models.TextField(blank=True, max_length=300),
        ),
    ]
