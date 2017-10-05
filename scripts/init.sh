#!/usr/bin/env bash

pip3 install virtualenv
gem install bundler
virtualenv venv
source venv/bin/activate

pip3 install -r requirements.txt
bundle install

ln -s conf/settings/local.py local_settings.py

createuser -s `whoami`
createdb -O `whoami` `whoami`

psql << EOF
CREATE ROLE {{ project_name }}_local WITH LOGIN ENCRYPTED PASSWORD '{{ project_name }}_local';
CREATE DATABASE {{ project_name }}_local WITH OWNER {{ project_name }}_local;
EOF

chmod +x manage.py
./manage.py migrate
