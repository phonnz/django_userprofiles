# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-20 13:42
from __future__ import unicode_literals

from django.db import migrations, models
import userprofiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name=b'Fecha de creaci\xc3\xb3n')),
                ('modified', models.DateTimeField(auto_now=True, verbose_name=b'Fecha de actualizaci\xc3\xb3n')),
                ('guid', models.CharField(blank=True, editable=False, max_length=100, null=True, verbose_name=b'Session token')),
                ('username', models.CharField(blank=True, max_length=50, null=True, unique=True, verbose_name=b'nombre de usuario')),
                ('email', models.EmailField(max_length=70, unique=True)),
                ('name', models.CharField(max_length=255, verbose_name=b'Nombre')),
                ('avatar', models.ImageField(blank=True, default=b'http://nyxstorage.blob.core.windows.net/telegana/2015_9_13_0_9_55_avatar.png', null=True, upload_to=b'/', verbose_name=b'Foto de perfil')),
                ('points', models.PositiveIntegerField(default=100, verbose_name=b'Puntos acumulados')),
                ('accept_terms', models.BooleanField(default=False, verbose_name=b'Aceptar T\xc3\xa9rminos y condiciones')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name=b'Creado')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name=b'Actualizado')),
                ('is_active', models.BooleanField(default=False, verbose_name=b'Verificado')),
                ('is_staff', models.BooleanField(default=False, verbose_name=b'Staff')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuario',
                'verbose_name_plural': 'Usuarios',
            },
            managers=[
                ('objects', userprofiles.models.UserManager()),
            ],
        ),
    ]
