# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-28 11:08
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0050_auto_20171128_1628'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='flow',
            new_name='flow1',
        ),
    ]
