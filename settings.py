import os

BASE = os.path.abspath(os.path.dirname(__name__))

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = ()

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.contrib.messages.context_processors.messages",
)

MANAGERS = ADMINS

TIME_ZONE = 'America/Los_Angeles'

LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True

USE_L10N = True

MEDIA_ROOT = ''

MEDIA_URL = '/media'

ADMIN_MEDIA_PREFIX = '/media/admin/'

TEMPLATE_DIRS = (
    os.path.join(BASE, "templates/"),
)

# Regenerate this.
SECRET_KEY = ''

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
    'django.middleware.transaction.TransactionMiddleware'
)

ROOT_URLCONF = 'pledge4good.urls'

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'app.backends.CustomAuthBackend',
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.admin',
    'app',
    'south',

    # 'storages',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'simple': {
            'format': '[%(levelname)s] %(module)s@%(lineno)s: %(message)s'
        },
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'app': {
            'handlers': ['console'],
            'level': "DEBUG",
            "propagate": False
        },
        'django.request': {
            'handlers': ['console', 'mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

LOGIN_REDIRECT_URL = '/'
LOGIN_URL = '/login'
LOGOUT_URL = '/logout'

BRAINTREE_MERCHANT_ID = ''
BRAINTREE_PUBLIC_KEY = ''
BRAINTREE_PRIVATE_KEY = ''

FACEBOOK_APP_ID = ''
FACEBOOK_APP_API_KEY = ''
FACEBOOK_APP_SECRET = ''
FACEBOOK_REGISTRATION_METADATA = {u'fields': u'[{"name": "name"}, {"name": "first_name"}, {"name": "last_name"}, {"type": "text", "name": "username", "description": "Username"}, {"name": "email"}, {"name": "password"}]'}

TWITTER_CONSUMER_SECRET = ''
TWITTER_CONSUMER_KEY = ''

# Make sure this is URL-encoded: e.g.
# TWITTER_CALLBACK_URL = 'http%3A%2F%2Fpledge4good.elmcitylabs.com%2Fregister%2Ftwitter%2Fcomplete'
TWITTER_CALLBACK_URL = ''

# EMAIL_BACKEND = "django_ses.SESBackend"

# S3-based file uploading
# DEFAULT_FILE_STORAGE = 'storages.backends.s3.S3Storage'

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
AWS_STORAGE_BUCKET_NAME = ''

from S3 import CallingFormat
AWS_CALLING_FORMAT = CallingFormat.SUBDOMAIN

try:
    from local_settings import *
except:
    pass
