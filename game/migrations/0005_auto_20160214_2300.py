# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 23:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0004_auto_20160214_2259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exit',
            name='to_room',
            field=models.OneToOneField(blank=True, on_delete=django.db.models.deletion.CASCADE, to='game.Room'),
        ),
    ]