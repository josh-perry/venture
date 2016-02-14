# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-14 22:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('game', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Exit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('room_1', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='room_1', to='game.Room')),
                ('room_2', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='room_2', to='game.Room')),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='exits',
            field=models.ManyToManyField(to='game.Exit'),
        ),
    ]