# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 22:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0002_auto_20160214_2250'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exit',
            name='room_1',
        ),
        migrations.RemoveField(
            model_name='exit',
            name='room_2',
        ),
        migrations.AddField(
            model_name='exit',
            name='to_room',
            field=models.OneToOneField(default=None, on_delete=django.db.models.deletion.CASCADE, to='game.Room'),
            preserve_default=False,
        ),
    ]
