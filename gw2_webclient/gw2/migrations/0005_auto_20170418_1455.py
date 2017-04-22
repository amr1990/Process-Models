# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 14:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gw2', '0004_auto_20170412_2135'),
    ]

    operations = [
        migrations.AddField(
            model_name='character',
            name='age',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='created',
            field=models.CharField(default=0, max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='deaths',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='profession',
            field=models.CharField(default=None, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='title',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='character',
            name='guild',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='character',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='character',
            name='race',
            field=models.CharField(max_length=10),
        ),
    ]
