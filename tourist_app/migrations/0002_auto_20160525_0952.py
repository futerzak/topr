# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-25 09:52
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tourist_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tourist',
            new_name='Turysta',
        ),
        migrations.AlterModelOptions(
            name='turysta',
            options={'verbose_name_plural': 'Tury\u015bci'},
        ),
    ]
