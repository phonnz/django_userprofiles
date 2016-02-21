# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 13:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userprofiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='slug',
            field=models.SlugField(default='newUser', unique=True, verbose_name=b'Slug'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default=b'newUser', max_length=50, unique=True, verbose_name=b'nombre de usuario'),
        ),
    ]