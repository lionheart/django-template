For information on how to use this project template, check out the [wiki](https://github.com/lionheart/django-template/wiki/Django-1.9).

Installation
============

You've cloned the repo or started a new project with the startproject command. Here's how you actually get started developing. These steps assume you have pip installed.

1. Install PyPy and virtualenv.

        $ brew install pypy
        $ pip_pypy install virtualenv

2. Then, start a virtualenv in the project directory.

        $ /usr/local/share/pypy/virtualenv venv-pypy
        $ . venv-pypy/bin/activate

3. Install the project requirements.

        ({{ project_name }}) $ with_gmp=no pip install -r requirements.txt
        # wait for a couple of minutes, hopefully nothing goes wrong!

4. Link the local project settings to local_settings.py.

        ({{ project_name }}) $ ln -s conf/settings/local.py local_settings.py

5. Create your local database. Make sure you run the [steps below](#postgresql-installation) if you haven't already installed PostgreSQL.

        $ psql
        postgres# CREATE ROLE {{ project_name }}_local WITH LOGIN ENCRYPTED PASSWORD '{{ project_name }}_local';
        postgres# CREATE DATABASE {{ project_name }}_local WITH OWNER {{ project_name }}_local;

    **Note**: If you get a `psql: FATAL:  role "YOUR_USERNAME" does not exist` error, just do the following to save yourself from having to write `--user postgres` every time you want to run `psql`. If, say, your username is `dan` on your development machine, you'd run the following:

        $ createuser -s dan # Create a superuser named `dan`
        $ createdb -O dan dan # Create a database for this user to log into.

    After doing this, re-run the psql commands in step 5.

6. Make manage.py executable and run migrations.

        ({{ project_name }}) $ chmod +x manage.py
        ({{ project_name }}) $ ./manage.py migrate

7. Set up the Git hooks.

        $ git_config/configure.sh

8. Start the local development server.

        ({{ project_name }}) $ sudo ./manage.py runserver 0.0.0.0:80
        Performing system checks...

        September 17, 2014
        Django version 1.9.6, using settings 'settings'
        Starting development server at http://0.0.0.0:80/
        Quit the server with CONTROL-C.

Map "local.makecreate.co" to 127.0.0.0 using DNS. If you haven't yet registered a domain, add the following line to your `/etc/hosts` file.

    127.0.0.1 local.{{ your_project_name }}.com

After you've done that, open your browser and navigate to "[local.{{ your_project_name }}.com](http://local.{{ your_project_name }}.com)". Your project is now running!

PostgreSQL Installation
-----------------------

If you're on a Mac and have [Homebrew](https://github.com/homebrew/homebrew) installed, we'll keep it simple.

    brew install postgresql

If you're in the mood for a longer read or have run into issues, here's a good [article](https://www.codefellows.org/blog/three-battle-tested-ways-to-install-postgresql) on how to install PostgreSQL on your system (covers Mac OS X, Windows, and Ubuntu).
