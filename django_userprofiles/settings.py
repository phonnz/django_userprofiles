"""
Django settings for django_userprofiles project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os, sys
from unipath import Path

BASE_DIR = Path(__file__).ancestor(2)
sys.path.append(BASE_DIR.child("apps"))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b3)vx%+cz-*g8^26#s6vmhv9af53l)rlf(=_furb_ax$-+sf4o'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

TEMPLATE_DIRS = [BASE_DIR.child('templates'),]

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'userprofiles',
    # 'web',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

AUTHENTICATION_BACKENDS = (
    'userprofiles.backends.EmailOrUsernameOrMobileModelBackend',
    'django.contrib.auth.backends.ModelBackend',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)



ROOT_URLCONF = 'django_userprofiles.urls'

WSGI_APPLICATION = 'django_userprofiles.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
  'default': {
      'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
      'NAME': 'django_userprofiles',                      # Or path to database file if using sqlite3.
      # The following settings are not used with sqlite3:
      'USER': 'root',
      'PASSWORD': 'adminadmin',
      'HOST': 'localhost',                      # Empty for localhost through domain sockets or '127.0.0.1' for localhost through TCP.
  }
}

AUTH_USER_MODEL = 'userprofiles.User'

GRAPPELLI_ADMIN_TITLE = 'User profiles'

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'es-MX'

TIME_ZONE = 'America/Mexico_City'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

EMAIL_BACKEND = 'djrill.mail.backends.djrill.DjrillBackend'

MANDRILL_API_KEY = 's_2BHQGrBLJ52g807hgbZw'
