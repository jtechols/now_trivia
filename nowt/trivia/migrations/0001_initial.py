# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('sessions', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('correct', models.IntegerField(default=0)),
                ('rounds', models.IntegerField(choices=[(5, 5), (10, 10), (20, 20), (50, 50), (100, 100), (1000, 1000)], default=0)),
                ('current_round', models.IntegerField(default=0)),
                ('show_title', models.BooleanField(default=True)),
                ('show_artist', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Song',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('song_name', models.CharField(max_length=255)),
                ('artist', models.CharField(max_length=255)),
                ('file_name', models.CharField(max_length=255)),
                ('album_number', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='UserSession',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('game', models.ForeignKey(to='trivia.Game')),
                ('session', models.ForeignKey(to='sessions.Session')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='songs_asked',
            field=models.ManyToManyField(to='trivia.Song'),
        ),
    ]
