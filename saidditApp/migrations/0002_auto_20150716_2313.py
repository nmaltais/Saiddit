# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saidditApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Subreddit',
            new_name='Subsaiddit',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='subreddit',
            new_name='subsaiddit',
        ),
        migrations.RenameField(
            model_name='user',
            old_name='name',
            new_name='username',
        ),
    ]
