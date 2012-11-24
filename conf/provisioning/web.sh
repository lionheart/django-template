#!/bin/sh
set -x

# Start an instance with this file via
# ec2-run-instances --key mykey --user-data-file django ami-XXXXXXX

yes | add-apt-repository ppa:nginx/stable
apt-get update
yes | apt-get install nginx memcached rsync libpq-dev python-dev libxslt1-dev libxml2-dev python-psycopg2 git-core redis-server postgresql-client inetutils-syslogd apache2-utils python-pip libevent-dev libgraphviz-dev python-pip

# Create the www project directory
mkdir -p /var/www/{{ project_name }}
chown -R ubuntu:ubuntu /var/www/{{ project_name }}

# Where to store rotated logs
mkdir -p /var/log/rotated

# Where SSL certificates should be stored
mkdir -p /etc/nginx/ssl

# Replace the default logrotation
rm /etc/logrotate.conf
ln -s /var/www/{{ project_name }}/conf/logrotate.conf /etc/

# Use a stripped down nginx configuration file
rm /etc/nginx/nginx.conf
ln -s /var/www/{{ project_name }}/conf/nginx/base.ngx /etc/nginx/nginx.conf

# Remove all existing enabled nginx sites
rm /etc/nginx/sites-enabled/*
ln -s /var/www/{{ project_name }}/conf/nginx/current.gunicorn.ngx /etc/nginx/sites-enabled/

pip install virtualenv
sudo -u ubuntu mkdir /home/ubuntu/environments/{{ project_name }}
sudo -u ubuntu virtualenv /home/ubuntu/environments/{{ project_name }}
pip install supervisor

