# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-08-14 15:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('taskoftheday', '0005_auto_20170814_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='task_img',
            field=models.ImageField(upload_to='taskoftheday/static/taskoftheday/img/uploads-tasks'),
        ),
    ]
