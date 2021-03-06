# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-13 13:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('taskoftheday', '0012_auto_20171013_1833'),
    ]

    operations = [
        migrations.AddField(
            model_name='usertask',
            name='current_step',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='taskoftheday.Step'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usertask',
            name='current_task',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='taskoftheday.Task'),
            preserve_default=False,
        ),
    ]
