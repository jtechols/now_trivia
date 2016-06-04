# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0002_auto_20160604_0506'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('number', models.IntegerField(default=1)),
                ('pub_year', models.IntegerField(default=1990)),
                ('pup_season', models.CharField(choices=[('FALL', 'Fall'), ('WNTR', 'Winter'), ('SPRG', 'Spring'), ('SUMR', 'Summer')], max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='song',
            name='album_number',
        ),
        migrations.AddField(
            model_name='song',
            name='album',
            field=models.ForeignKey(blank=True, to='trivia.Album', null=True),
        ),
    ]
