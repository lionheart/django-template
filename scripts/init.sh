#!/usr/bin/env bash

python3 -m venv venv/
source venv/bin/activate
python3 -m pip install -r requirements.txt

gem install bundler --no-force --no-document
bundle install

ln -s conf/settings/local.py local_settings.py

createuser -s `whoami`
createdb -O `whoami` `whoami`

psql << EOF
CREATE ROLE {{ project_name }}_local WITH LOGIN ENCRYPTED PASSWORD '{{ project_name }}_local';
CREATE DATABASE {{ project_name }}_local WITH OWNER {{ project_name }}_local;
EOF

chmod +x manage.py
./manage.py makemigrations app
./manage.py migrate

