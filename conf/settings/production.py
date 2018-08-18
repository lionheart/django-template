# -*- coding: utf-8 -*-

import os

DEBUG = 'DEBUG' in os.environ
TEMPLATE_DEBUG = DEBUG
BASE = os.path.abspath(os.path.dirname(__name__))

ALLOWED_HOSTS = [".{{ product_name }}.com", "{{ project_name }}.herokuapp.com"]

import dj_database_url
DATABASES = {'default': dj_database_url.config()}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

# Uncomment if you'd like to use S3 for static file storage.
# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# STATICFILES_STORAGE = 'statictastic.backends.VersionedS3BotoStorage'

DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'
STATICFILES_STORAGE = 'statictastic.backends.VersionedFileSystemStorage'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE, "templates"),
        ],
        'OPTIONS': {
            'loaders': (
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ),
            'context_processors': [
                "django.contrib.auth.context_processors.auth",
                "django.template.context_processors.debug",
                "django.template.context_processors.media",
                'django.template.context_processors.tz',
                "django.template.context_processors.request",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


BASE_URL = "https://{{ project_name }}.herokuapp.com"
