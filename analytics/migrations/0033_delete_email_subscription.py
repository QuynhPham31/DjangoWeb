# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-28 13:01
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('analytics', '0032_auto_20170928_1500'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Email_Subscription',
        ),
    ]
