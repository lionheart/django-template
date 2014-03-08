For information on how to use this project template, check out the [wiki](https://github.com/lionheart/django-template/wiki/Django-1.6).

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

5. Make manage.py executable and sync your local database.

        ({{ project_name }}) $ chmod +x manage.py
        ({{ project_name }}) $ ./manage.py syncdb

6. Start the server.

        ({{ project_name }}) $ sudo ./manage.py runserver
        Validating models...
        0 errors found

        Django version 1.5, using settings '{{ project_name }}.settings'
        Running django-devserver 0.5.0
        Threaded django server is running at http://0.0.0.0:80/
        Quit the server with CONTROL-C.

I generally map "local.{{ project_name }}.com" to 127.0.0.0 with my DNS service. If you haven't yet registered a domain, add the following line to your `/etc/hosts` file.

    127.0.0.1 local.{{ project_name }}.com

After you've done that, open your browser and navigate to "http://local.{{ project_name }}.com/".

