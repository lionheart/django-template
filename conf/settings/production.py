# -*- coding: utf-8 -*-

DEBUG = False
TEMPLATE_DEBUG = DEBUG

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'statictastic.backends.VersionedS3BotoStorage'

# Optionally change to full CDN url
STATIC_URL = "https://s3.amazonaws.com/{{ project_name }}-static/"
ADMIN_MEDIA_PREFIX = "https://s3.amazonaws.com/{{ project_name }}-static/admin/"

BASE_URL = "https://{{ project_name }}.com"
