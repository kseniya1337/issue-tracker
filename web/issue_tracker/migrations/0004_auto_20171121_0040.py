# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-20 21:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issue_tracker', '0003_auto_20171121_0037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='issue',
            name='status',
            field=models.CharField(choices=[('open', 'открыта'), ('in_progress', 'в разработке'), ('testing', 'в тестировании'), ('production', 'на боевом сервере'), ('closed', 'закрыта')], default='open', max_length=255, verbose_name='статус'),
        ),
    ]
