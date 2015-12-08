# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='forumuser',
            old_name='avater',
            new_name='avatar',
        ),
        migrations.RenameField(
            model_name='forumuser',
            old_name='self_info',
            new_name='self_intro',
        ),
        migrations.RenameField(
            model_name='forumuser',
            old_name='update',
            new_name='updated',
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='douban',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='github',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='forumuser',
            name='twitter',
            field=models.CharField(max_length=200, null=True, blank=True),
        ),
    ]
