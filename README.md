For information on how to use this project template, check out the [wiki](https://github.com/lionheart/django-template/wiki/Django-1.8).

Installation
============

You've cloned the repo or started a new project with the startproject command. Here's how you actually get started developing. I'm assuming you already have pip installed.

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

5. Make your local database.

        psql -d postgres
        create role {{ your_role_name }} with login encrypted password '{{ your_password }}';
        create database {{ your_database_name }} with owner {{ your_role_name }};

6. Sync your local database.

        ({{ project_name }}) $ chmod +x manage.py
        ({{ project_name }}) $ ./manage.py migrate

7. Start the server.
    ####With runserver
        ({{ project_name }}) $ sudo APP_ENVIRONMENT='local' ./manage.py runserver 0.0.0.0:80
        Performing system checks...

        September 17, 2014
        Django version 1.8, using settings 'settings'
        Starting development server at http://0.0.0.0:80/
        Quit the server with CONTROL-C.
    ####With livereload
        ({{ project_name }}) $ sudo APP_ENVIRONMENT='local' ./manage.py livereload

I generally map "local.{{ your_project_name }}.com" to 127.0.0.0 with my DNS service. If you haven't yet registered a domain, add the following line to your `/etc/hosts` file.

    127.0.0.1 local.{{ your_project_name }}.com

After you've done that, open your browser and navigate to "http://local.{{ your_project_name }}.com/".


PostgreSQL Setup
================

Here's a good [article](https://www.codefellows.org/blog/three-battle-tested-ways-to-install-postgresql) on how to install PostgreSQL on your system.
