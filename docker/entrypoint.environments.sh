#!/usr/bin/env sh

. /opt/cashstar/scripts/utils.sh

output_build_requirements

# we need our own copy of this file because we are downloading multiple settings files
verify_required_env_variables_set "SECRETS_BUCKET_NAME" "SECRETS_LOCAL_PATH" "SECRETS_LOCAL_FILE" "SECRETS_S3_KEY" "BASE_SETTINGS_MODULE"
download_settings_file "$SECRETS_BUCKET_NAME" "$SECRETS_LOCAL_PATH" "$SECRETS_LOCAL_FILE" "$SECRETS_S3_KEY"
download_settings_file "$SECRETS_BUCKET_NAME" "$SECRETS_LOCAL_PATH" "mutualauth.cashstar.com.jks" "consumer_api/mutualauth.cashstar.com.jks"

exec "$@"

