# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-27 22:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0002_auto_20151227_1624'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='0', verbose_name=b'Slug'),
            preserve_default=False,
        ),
    ]
