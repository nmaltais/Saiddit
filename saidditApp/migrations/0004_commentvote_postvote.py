# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('saidditApp', '0003_auto_20150718_1422'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.IntegerField(choices=[(1, b'up'), (2, b'down')])),
                ('comment', models.ForeignKey(to='saidditApp.Comment')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PostVote',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('direction', models.IntegerField(choices=[(1, b'up'), (2, b'down')])),
                ('post', models.ForeignKey(to='saidditApp.Post')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
