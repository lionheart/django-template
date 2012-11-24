Features
========

Libraries
---------

Includes a requirements.txt with libraries that promote Django best practices, such as:

* South, for database migrations.
* Django storages, for support with many file storage backends.
* Fabric, for easy deployments.
* Django Devserver, for a great replacement to the built in Django runserver command.
* Django Debug Toolbar, for an easy to use toolbar with fantastic profiling information.
* Statictastic, for an easy way to sync static media to your storage backends.

Deployment
----------

Included is a Fabric file that assumes you use your SSH configuration file to
manage your SSH keys.

Configuration
-------------

Baked in gunicorn, nginx, and supervisor configurations.

Get started
-----------

To start a new Django project called `project_name`, run the following.

    django-admin.py startproject -e md,ngx,ini --template=https://github.com/aurorasoftware/django-template/archive/django-1.4.zip project_name

Installation
============

You've cloned the repo or started a new project with the startproject command.
Here's how you actually get started developing. I'm assuming you already have
pip installed.

1. Install virtualenv

        pip install virtualenv

2. Then, start a virtualenv in the project directory.

        $ virtualenv .
        $ . bin/activate

3. Install the project requirements.

        ({{ project_name }}) $ pip install -r requirements.txt
        # wait for a couple of minutes, hopefully nothing goes wrong!

4. Link the local project settings to local_settings.py.

        ({{ project_name }}) $ ln -s conf/settings/local.py local_settings.py

5. Make manage.py executable and sync your local database.

        ({{ project_name }}) $ chmod +x manage.py
        ({{ project_name }}) $ ./manage.py syncdb

6. Run the server!

        ({{ project_name }}) $ sudo ./manage.py runserver
        Validating models...
        0 errors found

        Django version 1.4.2, using settings '{{ project_name }}.settings'
        Running django-devserver 0.4.0
        Threaded django server is running at http://0.0.0.0:80/
        Quit the server with CONTROL-C.

I generally map "local.{{ project_name }}.com" to 127.0.0.0 with my DNS. If you
haven't yet registered a domain, add the following line to your `/etc/hosts`
file.

    127.0.0.1 local.{{ project_name }}.com

After you've done that, open your browser and navigate to "http://local.{{ project_name }}.com/".

