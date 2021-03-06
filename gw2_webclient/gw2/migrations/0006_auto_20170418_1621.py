# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-04-18 16:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gw2', '0005_auto_20170418_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profession',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AlterField(
            model_name='character',
            name='profession',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gw2.Profession'),
        ),
        migrations.CreateModel(
            name='ProfessionTraining',
            fields=[
                ('profession_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='gw2.Profession')),
                ('trainingname', models.CharField(max_length=50)),
            ],
            bases=('gw2.profession',),
        ),
    ]
