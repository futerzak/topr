# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-25 09:48
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tourist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numer_telefonu', models.CharField(max_length=20)),
                ('pozycja_N', models.FloatField()),
                ('pozycja_E', models.FloatField()),
                ('ostatni_ruch', models.DateTimeField()),
            ],
        ),
    ]
