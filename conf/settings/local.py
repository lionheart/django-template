import os

BASE = os.path.abspath(os.path.dirname(__name__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '{{ project_name }}_local',
        'USER': '{{ project_name }}_local',
        'PASSWORD': '{{ project_name }}_local',
        'HOST': '127.0.0.1',
        'PORT': '5432'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '{{ project_name }}'
    }
}

RAVEN_CONFIG = {
    'dsn': ""
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'statictastic.backends.VersionedFileSystemStorage'

STATIC_URL = "/static/"

EMAIL_BACKEND = 'django.core.mail.backends.filebased.EmailBackend'
EMAIL_FILE_PATH = '/tmp/app-messages'

BASE_URL = "http://local.{{ project_name }}.com"
