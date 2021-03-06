# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-28 11:56
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django


class Migration(migrations.Migration):

    dependencies = [
        ('initial_avatars', '0001_initial'),
    ]

    if django.VERSION < (2, 0, 0):
        operations = [
            migrations.AlterField(
                model_name='Background',
                name='user',
                field=models.OneToOneField(
                    related_name='initial_avatars',
                    primary_key=True,
                    serialize=False,
                    to=settings.AUTH_USER_MODEL,
                    on_delete=models.CASCADE
                )
            ),
        ]

