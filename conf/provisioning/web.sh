#!/bin/sh
set -x

# Start an instance with this file via
# ec2-run-instances --key mykey --user-data-file django ami-XXXXXXX

yes | add-apt-repository ppa:nginx/stable
apt-get update
apt-get --yes install nginx memcached rsync libpq-dev python3-dev libxslt1-dev libxml2-dev python3-psycopg2 git-core redis-server postgresql postgresql-contrib inetutils-syslogd apache2-utils python3-pip libevent-dev libgraphviz-dev libffi-dev ruby-dev

# Uncomment if you want to install Wordpress
# yes | apt-get install php5-fpm php5-mysql mysql-server

# Create the www project directory
mkdir -p /var/www/{{ project_name }}
chown -R ubuntu:ubuntu /var/www/{{ project_name }}

# Where to store rotated logs
mkdir -p /var/log/rotated

# Where SSL certificates should be stored
mkdir -p /etc/nginx/ssl

# Replace the default logrotation
rm -f /etc/logrotate.conf
ln -s /var/www/{{ project_name }}/conf/logrotate.conf /etc/

# Use a stripped down nginx configuration file
rm -f /etc/nginx/nginx.conf
ln -s /var/www/{{ project_name }}/conf/nginx/base.ngx /etc/nginx/nginx.conf

# Remove all existing enabled nginx sites
rm -f /etc/nginx/sites-enabled/*
ln -s /var/www/{{ project_name }}/conf/nginx/$ENVIRONMENT.ngx /etc/nginx/sites-enabled/

pip3 install virtualenv
sudo -u ubuntu mkdir -p /home/ubuntu/environments/{{ project_name }}
sudo -u ubuntu virtualenv /home/ubuntu/environments/{{ project_name }}
pip3 install supervisor
pip3 install django
pip3 install setproctitle
pip3 install --upgrade pip

sudo gem install --no-rdoc --no-ri oily_png

