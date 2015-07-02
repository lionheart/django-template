# -*- coding: utf-8 -*-

DEBUG = False
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = [".{{ product_name }}.com"]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ project_name }}',
        'USER': '{{ project_name }}',
        'PASSWORD': '{{ project_name }}',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'statictastic.backends.VersionedS3BotoStorage'

# Optionally change to full CDN url
STATIC_URL = "/static/"

BASE_URL = "https://{{ project_name }}.com"
