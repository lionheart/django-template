FROM dwlz/lionheart-ubuntu:14.04

# apt-get update
# apt-get install -y python-setuptools nginx memcached libpq-dev python-dev python-psycopg2 postgresql-client inetutils-syslogd apache2-utils python-pip libevent-dev python-pip postgresql ruby ruby-dev
# gem install compass --no-ri --no-rdoc
# gem install oily_png --no-ri --no-rdoc

ADD . /var/www/{{ project_name }}

RUN cd /var/www/{{ project_name }} && pip install -r requirements.txt
RUN cd /var/www/{{ project_name }} && ln -s conf/settings/production.py local_settings.py
RUN cd /var/www/{{ project_name }} && compass compile --force
RUN chmod a+x /var/www/{{ project_name }}/manage.py

EXPOSE 80

# Do not run in production!
CMD ["/var/www/{{ project_name }}/manage.py", "runserver"]
