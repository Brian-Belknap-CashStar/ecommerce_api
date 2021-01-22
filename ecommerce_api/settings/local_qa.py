from .local import *
import cs_crypt


# DB/Redis settings
REDIS_HOST = 'services-redis.qa.cashstar.net'
REDIS_PORT = 6379
DATABASES = {
    'default': {
        'NAME': 'cashstardb',
        'ENGINE': 'django.db.backends.mysql',
        'USER': 'cashie_qa',
        'PASSWORD': 'cashie_123_qa',
        'HOST': 'db1.qa.cashstar.net',
        'PORT': '3306',
        'CONN_MAX_AGE': 0,
    },
}


# Rabbit MQ
_qa_broker = "amqp://cashstarqa:cash$tarqa@queue.qa.cashstar.net:5672//qa"
CELERY_BROKER_URL = BROKER_URL = _qa_broker

# Relevant QA service URLs
# TODO Once https://cashstar.atlassian.net/browse/DOPS-11715 is done we can stop requiring cs_crypt here
HTTP_USER_NAME = cs_crypt.decrypt('hu4rjMmVFfB0qtB9Tbayo3snM2WB3gV3/YJIM9W6UZKs0uM//O2GFz50V2aHglLuiGIY3rsB5ICb8WBdB/+5vHH8ggaQ6m0GZPPvgQECHtOGrVpp8xQRodXsRkuSNmOmhV4/53Mw1KRh2tFh7bvOA9WLwiQk03tP/XJjZMkohuuvo0pizYGddjcfkrLadS5GJCuUxgQS2n3/Rw8iTzLRu75LKBAOTPgNhz3mY5p5412Tux3ViOe3ErBtTt1AUZE7f8q6VhHVdzP2GKW6xNSPtsdTEliH/vR/I728dFMTiZKRYQy9fYJhExOzHDATHiRJ3I4NL6o+NiMr+XQuqvgSyQ==')
HTTP_PASSWORD = cs_crypt.decrypt('nHsNSG8j7clRI+8T0n+E0v2z0gLw9XOqKG/XiZkGsY/XxfN0rLVlVE6VkuevpzTqx6ZOUs1n4+LliurGV1jiY5iD6WMGNbHpOq9mggAZ7ovlZ1MMgIhoAUnfIQFV/5ryv4F6j5MBkLhZZ4nE19jWISFOMU3wNZRCh8IdbqmsB8h6fTy4GHn20C7VGmUa8O3QLkwUlNzs5D/n+TAmre8xk5yzV7u83m2AL1Zpth/XduAA1wedCV481YjcIoKOfH708Z1UDfR40TRrMpMDIWVu5WInEAFpRXYLNSs9lqwwQ7cqWZ0enp/RlADmY6xs3vMbr1zy/6WBlCte+KNuPKBXuw==')
CASHSTAR_ENVIRONMENT_DOMAIN = 'elb.us-east-1.qa.aws.cashstar.net'


KEYSTORE_PATH = "/opt/cashstar/configs/key/mutualauth.qa.cashstar.com.jks"
KEYSTORE_PASSWORD = cs_crypt.decrypt('Mu3VxmOm1AMse8qUn6TQvH8dLgWrMhMjjO+8HF9IUJHvq6yyyTRArNk0AYV8aqMvuPMsFEgDEH29iyjhzXOhk8Ox8lojFnARPaWrMMa3Dl2Omt0Rqso4HHCrx2kGf8H1piZRt3yaoJjaVp5m3C0iZFgKTV5UaRfqYf0Waois2/7bdK+3PpU4O0R221wEM1A6JKlvovCV4vDy0BZedVa2r3SYfet95kfZuA0QehY7n/lrRG7Rq1NR5trcLr6kCoyEHze1b2kaVHiza1Dy7hb5+sq4FG/XBv0gptE8588b1ADfCClT5fqaokSs20N60wJw9K/XXZ0qwV3Qk2WGG4oW1w==')

BHN_CATALOG_S3_BUCKET_NAME = 'drumall-bhn-catalogs-qa'
S3_BUCKET_CLIENTS_IMPORT = 'cashstar-business-clients-imports-qa'
