# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2017-07-26 15:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Guide',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('guide_category', models.CharField(max_length=70)),
                ('guide_why', models.TextField()),
                ('guide_how', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Step',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('guide', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskoftheday.Guide')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('task_img', models.ImageField(upload_to=b'')),
                ('task_task', models.TextField()),
                ('task_description', models.TextField()),
                ('step', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='taskoftheday.Step')),
            ],
        ),
    ]
