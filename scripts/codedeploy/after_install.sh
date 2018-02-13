#!/usr/bin/env bash

source /usr/local/etc/environments/{{ project_name }}/bin/activate

cd /var/www/{{ project_name }}

# Logrotate configuration
rm -f /etc/logrotate.conf
cp conf/logrotate.conf /etc/
cp conf/logrotate/* /etc/logrotate.d

rm -f /etc/cron.d/{{ project_name }}
cp conf/cron/production.crontab /etc/cron.d/{{ project_name }}

rm -f local_settings.py
ln -s conf/settings/production.py local_settings.py
rm -f conf/gunicorn/current.py
ln -s production.py conf/gunicorn/current.py

pip install -r requirements.txt
./manage.py migrate

sass --force --update --style compressed static/scss:static/css
./manage.py syncmedia --ignore=img-sources/

# TODO
sed -i"" -r -e "s/^COMMIT_SHA = .*$/COMMIT_SHA = '$DEPLOYMENT_ID'/g" settings.py

chown -R ubuntu:ubuntu /var/www/{{ project_name }}

