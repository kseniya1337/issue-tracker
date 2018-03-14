# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-06 19:33
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='assignee',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='issues', to=settings.AUTH_USER_MODEL, verbose_name='исполнитель'),
        ),
    ]