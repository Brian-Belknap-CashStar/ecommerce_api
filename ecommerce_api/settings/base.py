import os.path
import socket

from jet_setting.startup import external_settings_file_folder

ADMINS = [('Engineering Admin', 'webadmin@cashstar.com')]
MANAGERS = ADMINS
HOSTNAME = socket.gethostname()

settings_dir = os.path.dirname(__file__)
PROJECT_ROOT = os.path.abspath(os.path.dirname(settings_dir) + '/..')
PROJECT_NAME = 'Product Service'

LOCALE_PATHS = (
    os.path.join(PROJECT_ROOT, 'product_service/locale/'),
)

# NOTE: SECRET_KEY was moved to environment specific settings files

DEBUG = False

ALLOWED_HOSTS = ['*']

PREREQ_APPS = [
    'django.contrib.auth',
    'django_extensions',
    'django.contrib.sessions',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'django.contrib.staticfiles',
    'rest_framework',
    'raven.contrib.django.raven_compat',
]

PROJECT_APPS = [
    'test',
]

INSTALLED_APPS = PREREQ_APPS + PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.http.ConditionalGetMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cashstardb',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'America/New_York'
USE_I18N = True
USE_L10N = False

ROOT_URLCONF = 'urls'

SITE_ID = 1

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.request',
            ],
        },
    },
]

STATIC_URL = '/static/'

CACHES = {
    'default': {
        'BACKEND': 'django_elasticache.memcached.ElastiCache',
        'LOCATION': [
            '127.0.0.1:11211',
        ],
        'KEY_PREFIX': '',
        'VERSION': 1,
        'OPTIONS': {  # Maps to pylibmc "behaviors"
            'tcp_nodelay': True,
            'ketama': True,
        },
        'TIMEOUT': 10800,  # How long in seconds a key should live in memcached
        'BINARY': True,
    }
}

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d '
                      '%(thread)d %(message)s'
        },
        'simple': {
            'format': '%(levelname)s %(message)s'
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
    },
    'handlers': {
        'null': {
            'level': 'INFO',
            'class': 'logging.NullHandler',
        },
        'console': {
            'level': 'INFO',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        },
        'log_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/opt/cashstar/logs/apps/product_service.log',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10,
        },
        'bhn_log_file': {
            'level': 'INFO',
            'class': 'cloghandler.ConcurrentRotatingFileHandler',
            'formatter': 'verbose',
            'filename': '/opt/cashstar/logs/apps/bhn_sync_script.log',
            'maxBytes': 1024 * 1024 * 10,  # 10 MB
            'backupCount': 10
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'sentry': {
            'level': 'ERROR',
            'class': 'raven.contrib.django.handlers.SentryHandler',
        },
    },
    'loggers': {
        '': {
            'handlers': ['log_file', 'sentry'],
            'level': 'INFO',
            'propagate': False,
        },
        'django': {
            'handlers': ['log_file', 'sentry'],
            'level': 'INFO',
            'propagate': False,
        },
        'raven': {
            'level': 'DEBUG',
            'handlers': ['console', 'log_file'],
            'propagate': False,
        },
        'sentry.errors': {
            'level': 'DEBUG',
            'handlers': ['console', 'log_file'],
            'propagate': False,
        },
        'celery.redirected': {
            'level': 'DEBUG',
            'handlers': ['console', 'log_file', 'sentry'],
            'propagate': False,
        },
        'catalog_sync': {
            'level': 'DEBUG',
            'handlers': ['bhn_log_file', 'sentry'],
            'propagate': False,
        }
    }
}

SHELL_PLUS_POST_IMPORTS = (
    'cstar.shell_plus_overrides',
)
import warnings
warnings.filterwarnings("ignore", message='Overriding setting DATABASES can lead to unexpected behavior.')

REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    # Return native `Date` and `Time` objects in `serializer.data`
    'DATETIME_FORMAT': None,
    'DATE_FORMAT': None,
    'TIME_FORMAT': None,
    # Remove browsable API
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
    ),
}

DEPLOYMENT_ENVIRONMENT = 'NOT_PROD'

EMAIL_HOST = 'smtp.mandrillapp.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = 'PmUXzVqx5AhbHpoE__IHZw'
EMAIL_HOST_USER = 'developers@cashstar.com'

DEFAULT_FROM_EMAIL = "giftcards@cashstar.com"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

HTTP_USER_NAME = 'cashmin'
HTTP_PASSWORD = '8S1nGle!Plum03'

# toggles on/off routing request search query to slave
USE_SLAVE_FOR_API_REQUEST_SEARCH = True

VGC_URI_SCHEME = 'https'

#  Celery/RabbitMQ
CELERY_BROKER_HEARTBEAT = 30
CELERY_BROKER_CONNECTION_RETRY = True
BROKER_PROTOCOL = "pyamqp"
CELERY_BROKER_HOST = "localhost"
CELERY_BROKER_PORT = 5672
CELERY_BROKER_VHOST = "/"
CELERY_BROKER_USER = "guest"
CELERY_BROKER_PASSWORD = "guest"
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = "json"
CELERY_TASK_IGNORE_RESULT = True
CELERY_TASK_DEFAULT_QUEUE = "product"
CELERY_TASK_QUEUES = {
    "product": {
        "binding_key": "product",
        "queue_arguments": {},
        "durable": False
    },
    "credit_line_bulk_account_name": {
        "binding_key": "credit_line_bulk_account_name",
        "queue_arguments": {},
        "durable": False
    },
    'product_bhn_sync_script': {
        'binding_key': 'product_bhn_sync_script',
        'queue_arguments': {},
        'durable': False
    },
    'promo_catalog_sync': {
        'binding_key': 'promo_catalog_sync',
        'queue_arguments': {},
        'durable': False
    },
    'cold_stock_process_file': {
        'binding_key': 'cold_stock_process_file',
        'queue_arguments': {},
        'durable': False
    },
    'clients_import_process_file': {
        'binding_key': 'clients_import_process_file',
        'queue_arguments': {},
        'durable': False
    }
}
CELERY_TASK_DEFAULT_DELIVERY_MODE = 'transient'
CELERY_RESULT_PERSISTENT = False
# NOTE We want the process id to show in the log files, to aid debugging
CELERY_WORKER_LOG_FORMAT = ("%(asctime)s %(process)d %(processName)s %(name)s "
                            "%(funcName)s\n    %(levelname)s %(message)s")

CELERY_WORKER_TASK_LOG_FORMAT = ("%(asctime)s %(process)d %(processName)s %(name)s "
                                 "%(funcName)s\n    %(task_name)s(%(task_id)s) "
                                 "%(levelname)s %(message)s")

SYNC_CREDIT_LINE_CLIENT_NAME = True

BHN_API_URL = 'https://api.certification.blackhawknetwork.com'
BHN_API_CERT_KEY = 'a4j2tkq6zdn28q3y5q2k98dsq4_general'
PRODUCT_CATALOG_URL = 'productCatalogManagement/v1/productCatalogs'
PRODUCT_MANAGEMENT_URL = 'productManagement/v1'
PRODUCT_MANAGEMENT_API_CERT_KEY = '5g81hp8v4dkgj174gmc9mtvl31_integration'

REQUEST_ATTEMPTS_COUNT = 3
KEYSTORE_PASSWORD = None

from service_versioning.parse import get_build_info
SENTRY_RELEASE = get_build_info(PROJECT_ROOT, 'release')
SENTRY_TAGS = {'build': get_build_info(PROJECT_ROOT, 'version')}

# Moved hardcoded BHN_PRODUCT_PROCESSOR_CODE from sync script to settings.
# Values for QA/PROD and SEMI has overridden in aws_qa,aws_semi and prod_aws setting files
BHN_PRODUCT_PROCESSOR_CODE = 'BLACKHAWK-DS'
CLIENTS_IMPORT_S3_BUCKET_NAME = 'cashstar-business-clients-imports-test'
BLAST_PRODUCT_PROCESSOR_CODE = 'BLAST'

KEYSTORE_PATH = os.path.join(external_settings_file_folder[:-1]
                             if external_settings_file_folder.endswith(os.sep)
                             else external_settings_file_folder,
                             'mutualauth.cashstar.com.jks')
