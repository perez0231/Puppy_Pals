# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-31 17:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_app', '0004_remove_users_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='user_name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='users',
            name='last_name',
            field=models.CharField(default='exit', max_length=255),
            preserve_default=False,
        ),
    ]
