FROM ubuntu:14.04

ADD . /var/www/{{ project_name }}

RUN apt-get update
RUN apt-get install -y python-setuptools nginx memcached rsync libpq-dev python-dev libxslt1-dev libxml2-dev python-psycopg2 git-core redis-server postgresql-client inetutils-syslogd apache2-utils python-pip libevent-dev libgraphviz-dev python-pip postgresql ruby

RUN easy_install pip
RUN cd /var/www/{{ project_name }} && pip install -r requirements.txt
RUN cd /var/www/{{ project_name }} && ln -s conf/settings/local.py local_settings.py
RUN chmod a+x /var/www/{{ project_name }}/manage.py

EXPOSE 80
CMD ["/var/www/{{ project_name }}/manage.py", "runserver"]
