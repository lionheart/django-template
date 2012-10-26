import os

BASE = os.path.abspath(os.path.dirname(__name__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()
# SERVER_EMAIL = "hi@example.com"

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = False

USE_L10N = False

MEDIA_ROOT = os.path.join(BASE, "media")

MEDIA_URL = '/media/'

ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_DIRS = (
    os.path.join(BASE, "templates"),
)

STATICFILES_DIRS = (
    os.path.join(BASE, "static"),
)

SECRET_KEY = '{{ secret_key }}'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.transaction.TransactionMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = '{{ project_name }}.urls'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'django.contrib.webdesign',
    'app',
    'south',

    'debug_toolbar',
    'devserver',
    'statictastic',
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
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'

DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False
}

INTERNAL_IPS = ['127.0.0.1', '0.0.0.0']

DEVSERVER_IGNORED_PREFIXES = ['/media', '/__debug__']
DEVSERVER_MODULES = (
    'devserver.modules.sql.SQLRealTimeModule',
    'devserver.modules.sql.SQLSummaryModule',
    'devserver.modules.profile.ProfileSummaryModule',
)

# from S3 import CallingFormat
# from boto.s3.connection import OrdinaryCallingFormat
# AWS_CALLING_FORMAT = CallingFormat.PATH
# AWS_S3_CALLING_FORMAT = OrdinaryCallingFormat()
# AWS_S3_SECURE_URLS = True
# AWS_QUERYSTRING_AUTH = False

# AWS_STATIC_STORAGE_BUCKET_NAME = 'static.{{ project_name }}.com'
# AWS_STATIC_ACCESS_KEY_ID = ''
# AWS_STATIC_SECRET_ACCESS_KEY = ''
# AWS_HEADERS = {
#         'Cache-Control': "max-age:5, public"
#     }
# STATIC_URL = ""

# django-statictastic querystring support
# COMMIT_SHA = ""

# DEFAULT_FILE_STORAGE = 'storages.backends.s3boto.S3BotoStorage'
# AWS_ACCESS_KEY_ID = ''
# AWS_SECRET_ACCESS_KEY = ''

# EMAIL_BACKEND = "django_ses.SESBackend"
# AWS_SES_ACCESS_KEY_ID = ''
# AWS_SES_SECRET_ACCESS_KEY = ''

# SESSION_REDIS_PREFIX = "session"
# SESSION_ENGINE = 'redis_sessions.session'

# Sentry / Raven Configuration
# RAVEN_CONFIG = {
#     'dsn': 'https://b2022b456a1d44b3a7a3a2ce6dd11a6c:e336ae25fc0044028aa09a24526f9524@app.getsentry.com/2600'
# }

try:
    from local_settings import *
except ImportError:
    import logging
    logger = logging.getLogger(__name__)
    logger.error("Please link the appropriate settings file from the settings folder to `local_settings.py` in the project root.")

# Uncomment if using django-celery
# try:
#     import celeryconfig
# except ImportError:
#     import logging
#     logger = logging.getLogger(__name__)
#     logger.error("Please link the appropriate celeryconfig.py file from the settings/celery folder to `celeryconfig.py` in the project root.")

