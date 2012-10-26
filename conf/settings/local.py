DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '{{ project_name }}.db'
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': '{{ project_name }}'
    }
}

DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
STATICFILES_STORAGE = 'statictastic.backends.VersionedFileSystemStorage'

STATIC_URL = "/static/"
ADMIN_MEDIA_PREFIX = '/static/admin/'

