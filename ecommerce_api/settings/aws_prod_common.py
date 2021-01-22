from .base import *

API_INTEGRATION_REQUEST_EMAIL_ADDRESS = 'giftcards@cashstar.com'

BHN_API_URL = 'https://api.blackhawknetwork.com'

# Moved hardcoded BHN_PRODUCT_PROCESSOR_CODE from sync script to settings with correct value for a PROD env.
BHN_PRODUCT_PROCESSOR_CODE = 'BLACKHAWK-DS'

BHN_CATALOG_S3_BUCKET_NAME = 'drumall-bhn-catalogs-prod'
S3_BUCKET_CLIENTS_IMPORT = 'cashstar-business-clients-imports-prod'
