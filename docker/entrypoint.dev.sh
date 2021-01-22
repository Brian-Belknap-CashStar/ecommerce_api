#!/usr/bin/env sh

# this is the location where libraries could be pip installed in editable mode, and it will be included with
# intellij debugging and command line versions of debugging.  An example is included below with the library being
# included in the docker-compose.yml volumes entry. The checked in version of this file should only have the #! at
# the top and the exec "$@" at the bottom active.  Please don't commit and in PR please remind developers not to
# include any pip installs as other developers wouldn't use them.
#/opt/cashstar/app/bin/pip install -e /opt/cashstar/jet_setting

# uncomment the following line to bootstrap new items listed in the bootstrap, please don't commit the
# following line uncommented.
#/opt/cashstar/app/bin/pip install -r  /opt/cashstar/app/ecommerce_api/conf/requirements.txt

# Uncomment the following line to generate migrations, you can add the required args to control the name or make just
# an applications.  The line should be commented out before committed.
#/opt/cashstar/app/bin/python /opt/cashstar/app/ecommerce_api/package-manager/manage.py makemigrations

exec "$@"
