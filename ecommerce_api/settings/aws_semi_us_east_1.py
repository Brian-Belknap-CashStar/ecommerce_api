from .base import *

RETAIL_SERVICES_SITE_SUFFIX = '-biz.semi.cashstar.com'

API_INTEGRATION_REQUEST_EMAIL_ADDRESS = 'qateam@cashstar.com'

# Moved hardcoded BHN_PRODUCT_PROCESSOR_CODE from sync script to settings with correct value for SEMI env.
BHN_PRODUCT_PROCESSOR_CODE = 'BLACKHAWK-DS-TEST3P'

# Redefine BLAST processor code
BLAST_PRODUCT_PROCESSOR_CODE = 'BLAST-TEST3P'

BHN_CATALOG_S3_BUCKET_NAME = 'drumall-bhn-catalogs-semi'
S3_BUCKET_CLIENTS_IMPORT = 'cashstar-business-clients-imports-semi'
