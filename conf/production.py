# -*- coding: utf-8 -*-
DEBUG = False
TEMPLATE_DEBUG = DEBUG

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',
    }
}

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'blah',
        'USER': 'blah',
        'PASSWORD': 'blah',
        'HOST': '127.0.0.1',
        'PORT': '',
    }
}

