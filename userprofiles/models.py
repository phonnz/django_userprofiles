# -*- coding: utf-8 -*-
import datetime

from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
## If you don't need to replace special characters on your slugs
from django.template.defaultfilters import slugify
## More options for characters replacement
# from slughifi import slughifi as slugify

class UserManager(BaseUserManager):

    def _create_user(self, username, email, password, is_active, is_staff, is_superuser, **extra_fields):
        if not email:
            return ValueError('El email es un campo obligatorio')
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, is_active=is_active, is_staff=is_staff, is_superuser=is_superuser, **extra_fields)
        user.set_password(password)
        user.save(using = self._db)
        return user


	def create_user(self, username, email, password=None, **extra_fields):
		return self._create_user(username, email, password, False, False, False, **extra_fields)

    def create_superuser(self, username, email, password, **extra_fields):
        return self._create_user(username, email, password, True, True, True, **extra_fields)


class TimeStampModel(models.Model):

    created = models.DateTimeField('Fecha de creación', auto_now_add = True)
    modified = models.DateTimeField('Fecha de actualización', auto_now = True)

    class Meta:
        abstract = True

class User(AbstractBaseUser, PermissionsMixin, TimeStampModel):
    username = models.CharField('nombre de usuario', max_length=50, unique=True)
    slug = models.SlugField('Slug', unique = True)
    email = models.EmailField('email', max_length = 50, unique = True)
    # plain_pass = models.CharField(max_length=25, null=True, blank=True)
    first_name = models.CharField('Nombre', max_length = 100)
    last_name = models.CharField('Apellido Paterno', max_length = 100)
    mom_last_name = models.CharField('Apellido Materno', max_length = 100, null = True, blank = True)
    points = models.IntegerField('Puntos', default=100)
    avatar = models.ImageField('Avatar', upload_to='/', null = True, blank = True)
    certifier_document = models.FileField('Documento verificador', null = True , blank = True)
    # date_joined = models.DateTimeField('Fecha de registro', editable=False, auto_now_add=True)
    # updated = models.DateTimeField('Actualizado', editable = False, auto_now = True)

    objects = UserManager()

    is_active = models.BooleanField('Verificado', default=False)
    is_staff = models.BooleanField('Staff', default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.username)
        super(User, self).save(*args, **kwargs)


    def get_short_name(self):
        return self.username

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
