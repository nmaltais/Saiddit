# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saidditApp', '0004_commentvote_postvote'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentvote',
            name='direction',
            field=models.IntegerField(choices=[(-1, b'up'), (1, b'down')]),
        ),
    ]
