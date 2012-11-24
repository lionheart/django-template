#!/bin/bash

if [ -z "$ENVIRONMENT" ]; then
    echo "Please specify the deployment environment (staging|production). For instance:"
    echo "# export ENVIRONMENT=staging"
    exit 1
fi

yes | add-apt-repository ppa:nginx/stable
apt-get update
yes | apt-get install nginx memcached rsync libpq-dev python-dev libxslt1-dev libxml2-dev python-psycopg2 git-core redis-server postgresql-client inetutils-syslogd apache2-utils python-pip libevent-dev libgraphviz-dev python-pip

mkdir -p /var/www/{{ project_name }}
chown -R ubuntu:ubuntu /var/www/{{ project_name }}

mkdir -p /var/log/rotated
mkdir -p /etc/nginx/ssl

rm /etc/logrotate.conf
ln -s /var/www/{{ project_name }}/conf/logrotate.conf /etc/

rm /etc/nginx/nginx.conf
ln -s /var/www/{{ project_name }}/conf/nginx/base.ngx /etc/nginx/nginx.conf

rm /etc/nginx/sites-enabled/*
ln -s /var/www/{{ project_name }}/conf/nginx/$ENVIRONMENT.gunicorn.ngx /etc/nginx/sites-enabled/

pip install virtualenv
sudo -u ubuntu mkdir /home/ubuntu/environments/{{ project_name }}
sudo -u ubuntu virtualenv /home/ubuntu/environments/{{ project_name }}
pip install supervisor

