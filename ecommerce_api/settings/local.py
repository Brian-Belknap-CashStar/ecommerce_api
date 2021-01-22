from .base import *
import cs_crypt

# Env
DEBUG = True
TEMPLATES[0]['OPTIONS']['debug'] = True
CELERY_TASK_ALWAYS_EAGER = True

SERVER_NAME = "LOCAL"
DEPLOYMENT_ENVIRONMENT = 'LOCAL'
EMAIL_SUBJECT_PREFIX = '[LOCAL] Product Service - '
SECRET_KEY = 'local-01234567890123456789012345678901234567891234'

# Admin Settings
ADMINS = []
admin_email = os.environ.get('DJANGO_ADMIN_EMAIL', [])
if admin_email:  # Set the local admin E-mail if their environment variable is set
    ADMINS.append(("Local Admin", admin_email))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cashstardb',
        'USER': 'root',
        'PASSWORD': '',
        'HOST': 'localhost',
        'CONN_MAX_AGE': 0,
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

LOGGING['handlers']['log_file']['filename'] = '/tmp/product_service.log'
LOGGING['loggers']['']['handlers'] = ['console', 'log_file']
LOGGING['loggers']['django']['handlers'] = ['console', 'log_file']

RETAIL_SERVICES_SITE_SUFFIX = '-biz.qa.cashstar.com'
SYNC_CREDIT_LINE_CLIENT_NAME = False

# Relevant QA service URLs
# TODO Once https://cashstar.atlassian.net/browse/DOPS-11715 is done we can stop requiring cs_crypt here
HTTP_USER_NAME = cs_crypt.decrypt('hu4rjMmVFfB0qtB9Tbayo3snM2WB3gV3/YJIM9W6UZKs0uM//O2GFz50V2aHglLuiGIY3rsB5ICb8WBdB/+5vHH8ggaQ6m0GZPPvgQECHtOGrVpp8xQRodXsRkuSNmOmhV4/53Mw1KRh2tFh7bvOA9WLwiQk03tP/XJjZMkohuuvo0pizYGddjcfkrLadS5GJCuUxgQS2n3/Rw8iTzLRu75LKBAOTPgNhz3mY5p5412Tux3ViOe3ErBtTt1AUZE7f8q6VhHVdzP2GKW6xNSPtsdTEliH/vR/I728dFMTiZKRYQy9fYJhExOzHDATHiRJ3I4NL6o+NiMr+XQuqvgSyQ==')
HTTP_PASSWORD = cs_crypt.decrypt('nHsNSG8j7clRI+8T0n+E0v2z0gLw9XOqKG/XiZkGsY/XxfN0rLVlVE6VkuevpzTqx6ZOUs1n4+LliurGV1jiY5iD6WMGNbHpOq9mggAZ7ovlZ1MMgIhoAUnfIQFV/5ryv4F6j5MBkLhZZ4nE19jWISFOMU3wNZRCh8IdbqmsB8h6fTy4GHn20C7VGmUa8O3QLkwUlNzs5D/n+TAmre8xk5yzV7u83m2AL1Zpth/XduAA1wedCV481YjcIoKOfH708Z1UDfR40TRrMpMDIWVu5WInEAFpRXYLNSs9lqwwQ7cqWZ0enp/RlADmY6xs3vMbr1zy/6WBlCte+KNuPKBXuw==')
CASHSTAR_ENVIRONMENT_DOMAIN = 'elb.us-east-1.qa.aws.cashstar.net'
