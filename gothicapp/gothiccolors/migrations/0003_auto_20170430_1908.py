# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-30 19:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gothiccolors', '0002_auto_20170429_2301'),
    ]

    operations = [
        migrations.RenameField(
            model_name='corpus',
            old_name='wikipedia',
            new_name='more_info',
        ),
        migrations.AlterField(
            model_name='corpus',
            name='edition',
            field=models.IntegerField(null=True),
        ),
    ]
