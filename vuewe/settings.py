"""
Django settings for vuewe project.

Generated by 'django-admin startproject' using Django 3.0.7.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import sys
import sentry_sdk
import environ

from sentry_sdk.integrations.django import DjangoIntegration  


env = environ.Env(
    # set casting, default value
    DEBUG=(bool, False)
)
# reading .env file
environ.Env.read_env()
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ.get("DEBUG")

ALLOWED_HOSTS = ["https://clairevara.live", "clairevara.live", "127.0.0.1"]

LOGOUT_REDIRECT_URL = 'homepage'


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'aview.core',
    'aview.dashboard',
    'simple_mail',
    'ckeditor',
    'modeltranslation',
    'django_extensions'
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

ROOT_URLCONF = 'vuewe.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'vuewe.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        #sqllite
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),

      
    }
}


# if 'test' in sys.argv:
#     DATABASES['default'] = {'ENGINE': 'django.db.backends.postgresql','NAME':'NavaraDb','USER':'postgres','PASSWORD':'Akpobi101$$','HOST':'localhost','PORT':'5432'}

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
    ]


STATIC_ROOT = os.path.join('/home/navararl/public_html/static')


sentry_sdk.init(
    "https://699d5746e8f64d92b8fa27d6f0072ff6@o482405.ingest.sentry.io/5535764",
    traces_sample_rate=1.0
    )

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get("EMAIL_HOST")
EMAIL_PORT = os.environ.get("EMAIL_PORT")
EMAIL_USE_SSL = True
EMAIL_HOST_USER = os.environ.get("EMAIL_HOST_USER")
EMAIL_HOST_PASSWORD = os.environ.get("EMAIL_HOST_PASSWORD")
DEFAULT_FROM_EMAIL = 'Navara <noreply@navarar.live>'

SIMPLE_MAIL_USE_CKEDITOR = True
SIMPLE_MAIL_USE_MODELTRANSLATION = True
SIMPLE_MAIL_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_SECRET_ACCESS_KEY = os.environ.get("AWS_SECRET_ACCESS_KEY")
AWS_STORAGE_BUCKET_NAME = "clairevara"
AWS_S3_ENDPOINT_URL = "https://nyc3.digitaloceanspaces.com"
AWS_S3_OBJECT_PARAMETERS = {"CacheControl": "max-age=86400", "ACL": "public-read"}
AWS_LOCATION = "static"

STATIC_URL = f"https://{AWS_S3_ENDPOINT_URL}/{AWS_LOCATION}/"
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
PUBLIC_MEDIA_LOCATION = "media"
MEDIA_URL = f"https://{AWS_S3_ENDPOINT_URL}/{PUBLIC_MEDIA_LOCATION}/"
DEFAULT_FILE_STORAGE = "aview.core.backends.MediaRootS3BotoStorage"
STATICFILES_STORAGE = "aview.core.backends.StaticRootS3BotoStorage"
