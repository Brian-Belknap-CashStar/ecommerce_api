from .base import *

EMAIL_SUBJECT_PREFIX = "[{0}] PRODUCT TEST - ".format(HOSTNAME)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'TEST': {
            'NAME': 'default'
        },
    },
    'slave': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'slave',
        'TEST': {
            'MIRROR': 'default'
        },
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-unicorn',
        'KEY_PREFIX': '',
        'VERSION': 1
    }
}

COMPRESS_ENABLED = False
DEBUG = True

BROKER_BACKEND = 'memory'
CELERY_TASK_ALWAYS_EAGER = True

CASHSTAR_ENVIRONMENT_DOMAIN = 'invalid'


# disable running migrations in tests
class DisableMigrations(object):
    def __contains__(self, item):
        return True

    def __getitem__(self, item):
        return None

MIGRATION_MODULES = DisableMigrations()

API_INTEGRATION_REQUEST_EMAIL_ADDRESS = 'fake@cashstar.com'

SYNC_CREDIT_LINE_CLIENT_NAME = False
KEYSTORE_PASSWORD = 'password1q2w3e'
KEYSTORE_PATH = 'bhn_catalog/tests/test.jks'
PRODUCT_MANAGEMENT_API_CERT_KEY = '5g81hp8v4dkgj174gmc9mtvl31_integration'

LOGGING['handlers']['log_file']['filename'] = '/tmp/product_service.log'
LOGGING['handlers']['bhn_log_file']['filename'] = '/tmp/bhn_log_file.log'

SECRET_KEY = 'local-01234567890123456789012345678901234567891234'
