# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-25 10:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0002_auto_20160525_0952'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='turysta',
            name='id',
        ),
        migrations.AlterField(
            model_name='turysta',
            name='numer_telefonu',
            field=models.CharField(max_length=20, primary_key=True, serialize=False),
        ),
    ]
