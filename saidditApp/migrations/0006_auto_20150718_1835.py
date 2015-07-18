# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('saidditApp', '0005_auto_20150718_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvote',
            name='direction',
            field=models.IntegerField(choices=[(-1, b'up'), (1, b'down')]),
        ),
    ]
