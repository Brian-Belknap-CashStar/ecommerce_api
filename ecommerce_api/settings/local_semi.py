from .local import *
import cs_crypt


# DB/Redis settings
REDIS_HOST = 'services-redis.semi.cashstar.net'
REDIS_PORT = 6379
DATABASES = {
    'default': {
        'NAME': cs_crypt.decrypt('N5MKMlEScNOVCxrXdTAyL0dZwWAGBLx7BwawqqIUdCs/3Mh78yVkY3ORnTzhtf6dAVoUkya6jjLzSTEGIk5B6VmWMfHRSFXE2wgAQGyGasHTmlA5eog9OIVfaBjawlyokF2YsB2UmN7qxla6iUnfxpTGjvOZtPJvtlxQDUTA6n6dkwN0IlPP1ONEE63Ybcxs4GLm9knCYMMzBEVRdFTvpEnj89FH1bvE/ABHB+ov4NgNfJIHNLipfvg+1rPJdhmfh3yP7X4EiozxnZlKxb6KNw/iIEdxaPzjFMYyCnmYurEqt4iHY1FPYDHqo5KlTdX5GzeW9cCdcvGi3lXHlLaf6Q=='),
        'ENGINE': 'django.db.backends.mysql',
        'USER': cs_crypt.decrypt('OwlvJ5K8QY5MWYWEuBIidyh7qnhFDmpKBD0Om1Xs7DYeHzoNoGwMFk67QUQrsc84UjVMQQcVuZE41Y0xW4AY6MhTG9LyeAPT5sPhtSH5/BbAAeMyS5kkfzJ2jdH/F5pVqkF+BBVx7XoCh5yLWRg77zTR170dvtfsCU1q3GXmAPMmL0fslsGgI4dDASgsBeJ5FSEhW3k4zrnxzsyFF4oXLPC7uTDps7faFUOcSFvmKhrULPHk1nnwJPzQ1yE8es1wnpqYZcgjpa1rXzfExYg2OytKe6O76q27SJMXMbnnmThJuGL9mc2XjbP+wtjfAa3LrQvldTJkIJKxNwC8L11qRw=='),
        'PASSWORD': cs_crypt.decrypt('IETqwPMb/qa2L0mzjgXbw8zttZC36hUwHw7afi+cZhqnJR6dRu8QC6M05LyRaRoYJni+o1N2K089WNYjF6NR4niKYAB1h4BO99pF1kaAw3rLXIzpWtlmsmx5G/PACLsw1ku1ahUP9JjGWeRygd/4n2oBMECMXq1wWwferyrE2otUTTWqke8V3c2TDRuB4BUh7j8mLZ6gjxIuHQIs2B5tU9lFTyBNP8HTNNb+/ATHBim7wYf57TGLIuU6K4fHCYq4/jcc4K2orkzfOAk1wJsCUUZORV+2hebHW86dRVsC+yJS61Zz/VxVrGSTKoILJCGESt2EwqMiSkueZ9Ki1063iA=='),
        'HOST': cs_crypt.decrypt('ZbXunJBJTmthNow6hhmf6fo/Q36yyWuJi0LBvN4y1o9R/FoqE6oFCEVBXIrRFLp94bldJp4a4vS3/oomomCYDGTfhN81BZiM1Uh6vk54eFLp6+Dqd4nt5qui8HJh4JjcWTSFh2aLJ258+JFp7nVLrpSuLRSwUcWbZ8IZkCV8l4qYI/UD0uipAARQ00+o9XQmp1KnIkhCn9qzGPNTSXjzYGgQ035zTSgfmef5CHV46wAZimjL8n6VUshRiqJj8ttSZPXNbfFSuQSp4xzxAN8pnWMx9q14YzvTzR9TEzqLVV1oUffsufPfzBFRO32JaXCoNBvqIK+GEBY3Dt5ORMCSJw=='),
        'CONN_MAX_AGE': 30,
    },
}


# Rabbit MQ
CELERY_BROKER_HOST = 'queue.semi.aws'
CELERY_BROKER_PORT = 5672
CELERY_BROKER_VHOST = '/semi'
CELERY_BROKER_USERNAME = 'cashstarsemi'
CELERY_BROKER_PASSWORD = 'cash$tarsemi'
CELERY_BROKER_URL = '{protocol}://{username}:{password}@{host}:{port}/{vhost}'.format(
    protocol='amqp',
    username=CELERY_BROKER_USERNAME,
    password=CELERY_BROKER_PASSWORD,
    host=CELERY_BROKER_HOST,
    port=CELERY_BROKER_PORT,
    vhost=CELERY_BROKER_VHOST)

# Relevant SEMI service URLs
HTTP_USER_NAME = cs_crypt.decrypt('m70KYPx1wIEZu3Wr7flxXB6heGY1cQt1G2E7QYK5uJFb2vX7odIxOVlNGG5qIDkXydy/kh4vzGt+a/lCcGrcRQhj2Bpy+pXKA+Kf48BsBka8JvcSessbrJvsKXnVFnnxsnTYg7jg+paU8y2pHqHy2CZjvvlVW59IsWN2bx/qP8lv/10X0VzxdfkushspqmctnUO5DWa7iOPdErOm3ry24QySeHkwhlCU8y7o0qO549ElEGeWoeLmGubJypQMZSOHAV2Irx8pIZzSGeZ8EEjloBeZFjgfT0NL3/7Zgmx3aSNixfRboYPUnr7imo+LZWZXjvECY8zmLgciFsPqA8hG+A==')
HTTP_PASSWORD = cs_crypt.decrypt('J6OMX0v+tn5ASK+662EYw2wQE/nkEOtQt3MvxYR+WMy0Kl5skdBIqFrPwOXvAfb9571EYw8I92RFRrY47uCnntbn8JpTb83QQ82kLvG4qNEfZQVDIwLVqWtVaQJZnTr4fCBye3zLJkwRogCXkZjWrWeJKdBM2SEYQ+bGpWdOE0OuUyqo4lkYWKEjdlXzIfmMBo8LKSQW+aJzt2Qd4tU/zrdvu3LbKH7oEfrS7e8lfAOGwgcVMYB5p8icMwOL8szOVXt8XfTsQIEmRnQKQ2dj8OJjFubLckny9PwNceble4aShPcFWF1b1R4e1cS4TEORYAaax3Aaehg0Xalnak/uKg==')
CASHSTAR_ENVIRONMENT_DOMAIN = 'elb.us-east-1.semi.aws.cashstar.net'


SECRET_KEY = cs_crypt.decrypt('WQt6E+jISHKBmK/Ds+O7603tI4tF+J/t4t5fkTN0UUgzxFosvpEDoVfpapi4vnOLxA9wy/eAlx6wu07E/GiTVAih6ZFyJHxbHcCwwSLl4D7jcKtRdrW/d+6fo+CNfr1dhMxupJ3xg0qXNSjyj/IZzMchzvmOAjqKVrfJGXSqm3CiiNp/bmB8erdfHswcMKPnRlRs3g2zCSRoAbMt2iGCr4FhSJxE3KPfkGe+kP9G60NLpZv/pHHyIaqxcgu1E+YVPVZNeI+kvmwkluFATxytlxGy+127RbcPU7Nzwugy54I1+Jkc+6X9G35ogd7cdimSnIPmCCCVW0O/e4w45XSg0A==')
KEYSTORE_PATH = '/opt/cashstar/configs/key/mutualauth.semi.cashstar.com.jks'
KEYSTORE_PASSWORD = cs_crypt.decrypt(b'Um9XuXHzgmCo5hD8oXc02SR5qcGbkBuwpNCoxvXkedoUak3V4B0dNF6+f1yI09nKNRoYIxyRLtfA2zBpsQ6UsccB8xhjxpu7LZIwqy80lWlC/MC3o3QMI8IgAuDpimCVMcL9D/8ISl1j8gPsMThIm3U0LFogxB7gV7WsRKpnLWHi+IFpn0geeePc1dYB2ZOiMWpuQxcX4ViRn9sQt+K9iodBa8GADrxECxmsvR4MwBy/nxK9kiPsrCAwuNtPG8sOegaf4S2Lswfd1q+cZ3KMVTaHeeMPkQ1peLgDu/x+Yyg94m+n/xIChqWAUkvAHYd0y5vfk/6/0aNiaTl3IkYQ4g==')

S3_BUCKET_CLIENTS_IMPORT = 'cashstar-business-clients-imports-semi'
