import os
# from S3 import CallingFormat
# from boto.s3.connection import OrdinaryCallingFormat

BASE = os.path.abspath(os.path.dirname(__file__))

DEBUG = True

ADMINS = ()
# SERVER_EMAIL = "hi@examp.com"

MANAGERS = ADMINS
TIME_ZONE = 'UTC'
LANGUAGE_CODE = 'en-us'
SITE_ID = 1

WSGI_APPLICATION = "wsgi.application"

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_DIRS = (os.path.join(BASE, "static"),)
STATIC_ROOT = os.path.join(BASE, "collected")

SECRET_KEY = '{{ secret_key }}'

ALLOWED_HOSTS = [
    "local.{{ project_name }}.com",
    "{{ project_name }}.com"
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'urls'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
    'django.contrib.auth.hashers.BCryptPasswordHasher',
]

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.staticfiles',
    'app',
    'statictastic',
    # 'livereload',
    # 'django_object_actions',
    # 'sorl.thumbnail',
    # 'djcelery',
    # 'raven.contrib.django.raven_compat',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'INFO',
        'handlers': ['syslog', 'papertrail', 'sentry', 'console'],
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        }
    },
    'formatters': {
        'condensed': {
            'format': '[%(levelname)s] %(name)s#%(lineno)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'papertrail': {
            'format': ':[%(levelname)s] %(name)s#%(lineno)d: %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'condensed'
        },
        'syslog': {
            'level': 'INFO',
            'address': '/dev/log',
            'class': 'logging.handlers.SysLogHandler',
            'formatter': 'condensed',
            'filters': ['require_debug_false'],
        },
        'papertrail': {
            'level': 'INFO',
            'class': 'logging.handlers.SysLogHandler',
            'address': ('logs.papertrailapp.com', 22222),
            'filters': ['require_debug_false'],
            'formatter': 'papertrail',
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
            'filters': ['require_debug_false'],
        },
    },
   'loggers': {
        'sorl': {
            'handlers': ['syslog', 'console'],
            'propagate': False,
        },
        'raven': {
            'handlers': ['sentry'],
            'propagate': False
        },
#        'django.db.backends': {
#            'level': 'INFO',
#            'propagate': False,
#            'handlers': ['syslog', 'console', 'sentry'],
#        },
#        'django.request': {
#            'level': 'INFO',
#            'propagate': False,
#            'handlers': ['syslog', 'console', 'sentry'],
#        },
    },
}

if not os.path.exists('/dev/log'):
    del LOGGING['handlers']['syslog']['address']
    LOGGING['handlers']['syslog']['class'] = 'logging.StreamHandler'

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/account/login'
LOGOUT_URL = '/account/logout'

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

# Uncomment imports at top to enable S3 integration
#
# AWS_CALLING_FORMAT = CallingFormat.PATH
# AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
# AWS_S3_SECURE_URLS = True
# AWS_QUERYSTRING_AUTH = False
# AWS_GZIP = True

# AWS_STORAGE_BUCKET_NAME = 'uploads-{{ project_name }}'
# AWS_STATIC_STORAGE_BUCKET_NAME = 'static-{{ project_name }}'
# AWS_HEADERS = {
#         'Cache-Control': "max-age:86400, public"
# }

# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''

# EMAIL_BACKEND = "django_ses.SESBackend"
# AWS_SES_ACCESS_KEY_ID = ''
# AWS_SES_SECRET_ACCESS_KEY = ''

# SESSION_REDIS_PREFIX = "session"
# SESSION_ENGINE = 'redis_sessions.session'

# SENTRY_PUBLIC_KEY = ""
# SENTRY_SECRET_KEY = ""
# RAVEN_CONFIG = {
#     'dsn': "https://{}:{}@app.getsentry.com/4195".format(SENTRY_PUBLIC_KEY, SENTRY_SECRET_KEY)
# }

# django-statictastic querystring support
COMMIT_SHA = ""

try:
    from local_settings import *
except ImportError:
    raise ImportError("""Please link the appropriate settings file from conf/settings to `local_settings.py` in the project root. E.g.

    ({{ project_name }})$ ln -s conf/settings/local.py local_settings.py""")

# Uncomment if using django-celery
# try:
#     import djcelery
#     djcelery.setup_loader()
#     import celeryconfig
# except ImportError:
#    raise ImportError("""Please link the appropriate settings file from conf/settings/celery to `celeryconfig.py` in the project root. E.g.
#
#    ({{ project_name }})$ ln -s conf/settings/celery/local.py celeryconfig.py""")

