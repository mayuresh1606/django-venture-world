"""
Django settings for venture_world project.

Generated by 'django-admin startproject' using Django 3.2.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""
import dj_database_url
import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-8$)fqb2#@xyc+ghdm689$v##@vwjy*2(0o-o)_%+9okcnkyb-u'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False
DEBUG_PROPAGATE_EXCEPTIONS = True

ALLOWED_HOSTS = [
    'venture-world.herokuapp.com',
    '127.0.0.1:8000',
    '127.0.0.1',
    'ventureworld.org'
]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'whitenoise.runserver_nostatic',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'tours.apps.ToursConfig',
    'storages',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'venture_world.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'venture_world.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {

    'default': {

        'ENGINE': 'django.db.backends.postgresql',

        'NAME': 'DEMO_TEST',

        'USER': 'postgres',

        'PASSWORD': 'maddy865210',

        'HOST': 'localhost',

        'PORT': '5432',

    }

}
db_from_env = dj_database_url.config(conn_max_age=600)
DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/

STATIC_URL = '/static/tours/'

STATIC_ROOT = os.path.join(BASE_DIR, 'static')

MEDIA_ROOT = os.path.join(BASE_DIR, '/static/images')

MEDIA_URL = 'https://s3.console.aws.amazon.com/s3/buckets/venture-world?region=ap-south-1&prefix=static/images/&showversions=false/'


# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# https://myaccount.google.com/lesssecureapps?pli=1&rapt=AEjHL4PquYTdw3PqNfHNVfOiCG7EquiwsiVw0QJo2AzpPaXYqSxOFcBESH_Tb7f5jw733DVnktYrN2UDy78VQb62ocuV616_cg


EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = '587'
EMAIL_HOST_USER = 'mayureshovhal1606@gmail.com'
EMAIL_HOST_PASSWORD = 'jmmlwehzmfhnhseh'
EMAIL_USE_TLS = True
# EMAIL_USE_SSL = False


# S3 BUCKETS CONFIG
AWS_ACCESS_KEY_ID = 'AKIAYYGWRM3XHKMGQKFU'
AWS_SECRET_ACCESS_KEY = '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'
AWS_STORAGE_BUCKET_NAME = 'venture-world'
AWS_S3_FILE_OVERWRITE = False
AWS_DEFAULT_ACL = None
AWS_S3_HOST = 's3.ap-south-1.amazonaws.com'
AWS_S3_REGION_NAME = "ap-south-1"
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
# STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'


'''
<?xml version="1.0" encoding="UTF-8"?>
<CORSConfiguration xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
<CORSRule>
    <AllowedOrigin>*</AllowedOrigin>
    <AllowedMethod>GET</AllowedMethod>
    <AllowedMethod>POST</AllowedMethod>
    <AllowedMethod>PUT</AllowedMethod>
    <AllowedHeader>*</AllowedHeader>
</CORSRule>
</CORSConfiguration>
'''
