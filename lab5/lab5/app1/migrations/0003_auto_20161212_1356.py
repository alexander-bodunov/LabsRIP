# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-12 10:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_good_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='good',
            name='title',
            field=models.CharField(max_length=40),
        ),
    ]
