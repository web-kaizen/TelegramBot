"""
Django settings for core project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""

import os
from pathlib import Path
import environ
import logging

env = environ.Env(
    DEBUG=bool,
    SECRET_KEY=str,
    NEED_LOGGER=bool,

    # Core
    APP_ID=str,
    THIRD_PARTY_APP_URL=str,

    # Redis
    REDIS_HOST=str,
    REDIS_PORT=int,
    CACHE_DEFAULT_TTL=int,

    # Postgres
    POSTGRES_DB_NAME=str,
    POSTGRES_DB_USER=str,
    POSTGRES_DB_PASSWORD=str,
    POSTGRES_DB_HOST=str,
    POSTGRES_DB_PORT=int,
    LOCALHOST=str,
    ALLOWED_HOSTS=str,
    INTERNAL_IPS=str
)

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Take environment variables from .env file
environ.Env.read_env(BASE_DIR / '.env')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = env('SECRET_KEY')
# SECRET_KEY = 'django-insecure-j021i7o-)w$0jb7@vls7^$*7@*gl0pr!h4i3^eds$v$500t25s'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = env('DEBUG')

LOCALHOST = env('LOCALHOST')
BASE_URI = "/api/v0"
ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(', ')

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    "rest_framework",
    'rest_framework_swagger',
    'drf_yasg',

    "core",
    "services",
    "telegram_bot"
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

dbHost: str = ""
if os.getenv('DOCKER_CONTAINER'):
    dbHost = env("POSTGRES_DB_HOST")
else:
    dbHost = "localhost"

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': env("POSTGRES_DB_NAME"),
        'USER': env("POSTGRES_DB_USER"),
        'PASSWORD': env("POSTGRES_DB_PASSWORD"),
        'HOST': dbHost,
        'PORT': env("POSTGRES_DB_PORT"),
    }
}
# Logger
NEED_LOGGER = env("NEED_LOGGER")

# Internal IPS
INTERNAL_IPS = env("INTERNAL_IPS").split(", ")

# Yadro
APP_ID = env('APP_ID')
THIRD_PARTY_APP_URL = env('THIRD_PARTY_APP_URL')

# Redis
REDIS_HOST = env('REDIS_HOST')
REDIS_PORT = env('REDIS_PORT')
CACHE_DEFAULT_TTL = env('CACHE_DEFAULT_TTL')

# Cache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': f'redis://{REDIS_HOST}:{REDIS_PORT}',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
# logging file system
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'main_formatter': {
            'format': '{asctime} - {levelname} - {module} - {filename} - {message}',
            'style': '{',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        }
    },
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
            'formatter': 'main_formatter'
        },
        'file': {
            'class': 'logging.FileHandler',
            'formatter': 'main_formatter',
            'filename': f'{BASE_DIR}/core/logs.log'
        }
    },
    'loggers': {
        'logger': {
            'handlers': ['console', 'file'],
            'level': 'INFO',
            'propagate': True
        }
    }
}

# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/


STATIC_URL = 'static/'

CORS_ALLOWED_ORIGINS = env("CORS_ALLOWED_ORIGINS").split(", ")

CORS_ORIGIN_ALLOW_ALL = True
# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

""" ASGI SETTINGS DJANGO"""
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_asgi_application()

""" WSGI SETTINGS DJANGO """
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
application = get_wsgi_application()

WSGI_APPLICATION = 'core.settings.application'
