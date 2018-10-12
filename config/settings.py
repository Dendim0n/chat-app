"""
Django settings for wayup project.

Generated by 'django-admin startproject' using Django 1.8.4.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

import os
from sys import path as sys_path

from configurations import Configuration, values
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))
sys_path.append(os.path.join(BASE_DIR, 'apps'))


class Common(Configuration):
    # Quick-start development settings - unsuitable for production
    # See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

    # SECURITY WARNING: keep the secret key used in production secret!
    SECRET_KEY = 'lw0g#zezc$vau!nn7#9kgtoi^=e^7!kg1^m_gaokak_=12d66e'

    # SECURITY WARNING: don't run with debug turned on in production!
    DEBUG = True

    ALLOWED_HOSTS = values.ListValue([])

    CHAT_WS_SERVER_HOST = values.Value('0.0.0.0')
    CHAT_WS_SERVER_PORT = values.IntegerValue(5002)

    # Application definition
    DJANGO_APPS = (
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.humanize',
        'django.contrib.sessions',
        'django.contrib.messages',
        'django.contrib.staticfiles',
    )

    VENDOR_APPS = (
        'crispy_forms',
        'django_extensions',
    )

    PROJECT_APPS = (
        'chat',
        'home',
    )

    INSTALLED_APPS = DJANGO_APPS + VENDOR_APPS + PROJECT_APPS

    MIDDLEWARE_CLASSES = (
        'django.contrib.sessions.middleware.SessionMiddleware',
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.contrib.auth.middleware.AuthenticationMiddleware',
        'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
        'django.contrib.messages.middleware.MessageMiddleware',
        'django.middleware.clickjacking.XFrameOptionsMiddleware',
        'django.middleware.security.SecurityMiddleware',
    )

    ROOT_URLCONF = 'config.urls'

    TEMPLATES = [
        {
            'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [
                'templates'
            ],
            'APP_DIRS': True,
            'OPTIONS': {
                'context_processors': [
                    'django.template.context_processors.debug',
                    'django.template.context_processors.request',
                    'django.contrib.auth.context_processors.auth',
                    'django.contrib.messages.context_processors.messages',
                ],
            },
        },
    ]

    WSGI_APPLICATION = 'config.wsgi.application'


    # Database
    # https://docs.djangoproject.com/en/1.8/ref/settings/#databases

    DATABASES = {
        'default': dj_database_url.config(
            default="sqlite:///{}".format(
                os.path.join(BASE_DIR, 'db.sqlite3')
            )
        )
    }


    # Internationalization
    # https://docs.djangoproject.com/en/1.8/topics/i18n/

    LANGUAGE_CODE = 'en-us'

    TIME_ZONE = values.Value('America/New_York')

    USE_I18N = True

    USE_L10N = True

    USE_TZ = values.BooleanValue(True)

    # Static files (CSS, JavaScript, Images)
    # https://docs.djangoproject.com/en/1.8/howto/static-files/

    STATIC_ROOT = os.path.join(BASE_DIR, 'public')
    STATIC_URL = '/static/'
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
    # STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

    MEDIA_URL = '/media/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

    LOGGING = {
        'version': 1,
        'disable_existing_loggers': True,
        'formatters': {
            'verbose': {
                'format':
                    '%(levelname)s %(asctime)s %(module)s'
                    ' %(process)d %(thread)d %(message)s'
            },
            'simple': {
                'format': '%(levelname)s %(message)s'
            },
        },
        'handlers': {
            'null': {
                'level': 'DEBUG',
                'class': 'django.utils.log.NullHandler',
            },
            'console': {
                'level': 'DEBUG',
                'class': 'logging.StreamHandler',
                'formatter': 'simple'
            },
            'mail_admins': {
                'level': 'ERROR',
                'class': 'django.utils.log.AdminEmailHandler',
            }
        },
        'loggers': {
            'django': {
                'handlers': ['null'],
                'propagate': True,
                'level': 'INFO',
            },
            'django.request': {
                'handlers': ['mail_admins'],
                'level': 'ERROR',
                'propagate': False,
            },
            'apps.home': {
                'handlers': ['console', 'mail_admins'],
                'level': 'INFO',
            },
            'apps.chat': {
                'handlers': ['console', 'mail_admins'],
                'level': 'DEBUG',
            }
        }
    }


class Development(Common):
    DEBUG = True


class Staging(Common):
    DEBUG = True


class Production(Common):
    DEBUG = False
