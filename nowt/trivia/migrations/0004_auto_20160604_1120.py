# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trivia', '0003_auto_20160604_1024'),
    ]

    operations = [
        migrations.RenameField(
            model_name='album',
            old_name='pup_season',
            new_name='pub_season',
        ),
    ]
