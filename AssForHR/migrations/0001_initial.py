# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-02-18 19:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EX_SourceSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('model_name', models.CharField(max_length=40)),
                ('source_table_name', models.CharField(max_length=40)),
                ('source_col_name', models.CharField(max_length=40)),
                ('source_version_name', models.CharField(max_length=40)),
            ],
        ),
    ]