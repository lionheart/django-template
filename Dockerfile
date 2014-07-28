FROM dwlz/lionheart-ubuntu:14.04

ADD . /var/www/{{ project_name }}

RUN easy_install pip
RUN cd /var/www/{{ project_name }} && pip install -r requirements.txt
RUN cd /var/www/{{ project_name }} && ln -s conf/settings/production.py local_settings.py
RUN cd /var/www/{{ project_name }} && compass compile --force
RUN chmod a+x /var/www/{{ project_name }}/manage.py

EXPOSE 80

# Do not run in production!
CMD ["/var/www/{{ project_name }}/manage.py", "runserver"]
