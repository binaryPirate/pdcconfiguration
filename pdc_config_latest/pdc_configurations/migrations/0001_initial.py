# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='configuration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('config', models.CharField(max_length=100)),
                ('status', models.CharField(default='pending', max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('host_name', models.CharField(max_length=100)),
                ('usrname', models.CharField(max_length=30)),
                ('passwd', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='srcdest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('source', models.CharField(max_length=1000)),
                ('destination', models.CharField(max_length=1000)),
            ],
        ),
    ]