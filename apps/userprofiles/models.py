# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
## If you don't need to replace special characters on your slugs
from django.template.defaultfilters import slugify
## More options for characters replacement
# from slughifi import slughifi as slugify
from django.core.validators import RegexValidator

def make_slug(self):
    if not self.slug or self.slug == 'newUser' :
        self.slug = slugify(self.username)
    else:
        self.slug = slugify(self.slug)

class UserManager(BaseUserManager):
    use_in_migrations = True

    def _create_user(self, username, email, password, **extra_fields):
        """
        Creates and saves a User with the given username, email and password.
        """
        print 'stat creations'
        if not email:
            raise ValueError('El email es un campo obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)
        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self._create_user(username, email, password, **extra_fields)


class TimeStampModel(models.Model):

    created = models.DateTimeField('Fecha de creación', auto_now_add = True)
    modified = models.DateTimeField('Fecha de actualización', auto_now = True)

    class Meta:
        abstract = True

class User(AbstractBaseUser, PermissionsMixin):
    guid = models.CharField('Session token', max_length=100, null = True, blank = True, editable = False)
    username = models.CharField('nombre de usuario', max_length=50, unique=True, null = True, blank = True)
    slug = models.SlugField('Slug', unique = True, default='newUser')
    email = models.EmailField('Email', max_length = 70, unique = True)
    mobile = models.CharField('Número móvil', max_length = 10, validators = [RegexValidator(regex='^[0-9]*$', message ='Escriba su número celular en 10 dígitos')], blank = True, null = True)
    name = models.CharField(max_length = 255, verbose_name = 'Nombre')
    avatar = models.ImageField(verbose_name = 'Foto de perfil', upload_to='/', null = True, blank = True, default = 'http://nyxstorage.blob.core.windows.net/telegana/2015_9_13_0_9_55_avatar.png', )#storage=AzureBlobStorage('telegana'))
    points = models.PositiveIntegerField(verbose_name = 'Puntos acumulados', default = 100)
    accept_terms = models.BooleanField(verbose_name = 'Aceptar Términos y condiciones', default=False)
    date_joined = models.DateTimeField(verbose_name = 'Creado', editable = False, auto_now_add = True)
    updated = models.DateTimeField(verbose_name = 'Actualizado', editable = False, auto_now = True)
    is_active = models.BooleanField('Verificado', default=False)
    is_staff = models.BooleanField('Staff', default=False)

    # username = models.CharField('nombre de usuario', max_length=50, unique=True)
    # email = models.EmailField('email', max_length = 50, unique = True)
    # slug = models.SlugField('Slug', unique = True)
    # # plain_pass = models.CharField(max_length=25, null=True, blank=True)
    # first_name = models.CharField('Nombre', max_length = 100, validators = [RegexValidator(regex='^[a-zA-Z]*$', message ='Solo pueden ser letras')])
    # last_name = models.CharField('Apellido Paterno', max_length = 100, validators = [RegexValidator(regex='^[a-zA-Z]*$', message ='Solo pueden ser letras')])
    # mom_last_name = models.CharField('Apellido Materno', max_length = 100, null = True, blank = True)
    # points = models.IntegerField('Puntos', default=100)
    # avatar = models.ImageField('Avatar', upload_to='/', null = True, blank = True)
    # certifier_document = models.FileField('Documento verificador', null = True , blank = True)


    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'mobile']

    def save(self, *args, **kwargs):
        make_slug(self)
        super(User, self).save(*args, **kwargs)


    def get_short_name(self):
        return self.username

    



    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
