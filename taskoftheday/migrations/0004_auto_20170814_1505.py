# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-14 15:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('taskoftheday', '0003_auto_20170727_1115'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_img',
            field=models.ImageField(upload_to='taskoftheday/static/taskoftheday/img/uploads-tasks'),
        ),
    ]
