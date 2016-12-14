# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-05-21 11:06
from __future__ import unicode_literals

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Deszcz',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopien', models.IntegerField(validators=django.core.validators.MinValueValidator(1))),
                ('deszcz_minimalny', models.IntegerField(validators=django.core.validators.MinValueValidator(0))),
                ('deszcz_maksymalny', models.IntegerField(validators=django.core.validators.MinValueValidator(0))),
            ],
        ),
        migrations.CreateModel(
            name='Lawina',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopien', models.IntegerField(validators=django.core.validators.MinValueValidator(1))),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Mgla',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopien', models.IntegerField(validators=django.core.validators.MinValueValidator(1))),
                ('opis', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Pogoda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('czas', models.DateTimeField()),
                ('deszcz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Deszcz')),
                ('lawina', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Lawina')),
                ('mgla', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Mgla')),
            ],
        ),
        migrations.CreateModel(
            name='StanAlarmowy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('poziom', models.IntegerField(validators=django.core.validators.MinValueValidator(1))),
                ('dzialanie', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Szlak',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('KML', models.TextField()),
                ('trudnosc', models.IntegerField(validators=django.core.validators.MinValueValidator(1))),
                ('kolor', models.CharField(choices=[('zo', '\u017c\xf3\u0142ty'), ('n', 'niebieski'), ('z', 'zielony'), ('cza', 'czarny'), ('cze', 'czerwony')], max_length=255)),
                ('pogoda', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Pogoda')),
                ('stan_alarmowy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.StanAlarmowy')),
            ],
        ),
        migrations.CreateModel(
            name='Temperatura',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopien', models.IntegerField(validators=django.core.validators.MinValueValidator(1))),
                ('minimalna_ujemna', models.IntegerField(validators=django.core.validators.MaxValueValidator(-1))),
                ('maksymalna_ujemna', models.IntegerField(validators=django.core.validators.MaxValueValidator(-1))),
                ('minimalna_dodatnia', models.IntegerField(validators=django.core.validators.MinValueValidator(0))),
                ('maksymalna_dodatnia', models.IntegerField(validators=django.core.validators.MinValueValidator(0))),
            ],
        ),
        migrations.CreateModel(
            name='Wiatr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stopien', models.IntegerField(validators=django.core.validators.MinValueValidator(1))),
                ('predkosc_minimalna', models.IntegerField(validators=django.core.validators.MinValueValidator(0))),
                ('predkosc_maksymalna', models.IntegerField(validators=django.core.validators.MinValueValidator(0))),
            ],
        ),
        migrations.AddField(
            model_name='pogoda',
            name='temperatura',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Temperatura'),
        ),
        migrations.AddField(
            model_name='pogoda',
            name='wiatr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Wiatr'),
        ),
        migrations.AddField(
            model_name='deszcz',
            name='wiatr',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system_app.Wiatr'),
        ),
    ]