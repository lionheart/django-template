To start a new Django project called `project_name`, run the following.

    django-admin.py startproject -e md,ngx,ini --template=https://github.com/aurorasoftware/django-bootstrap/archive/django-1.4.zip project_name

Installation
============

You've cloned the repo or started a new project with the startproject command.
Here's how you actually get started developing. I'm assuming you already have
pip installed.

1. If pip is installed, the next thing you have to do is install virtualenv

        pip install virtualenv

2. Then, start a virtualenv in the project directory.

        $ virtualenv .

3. Install the project requirements.

        ({{ project_name }}) $ pip install -r requirements.txt
        # wait for a couple of minutes, hopefully nothing goes wrong!

4. Link the local project settings to local_settings.py.

        ({{ project_name }}) $ ln -s conf/settings/local.py local_settings.py

5. Sync your local database.

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

After you've done that, open your browser, navigate to "http://local.{{ project_name }}.com/",
and start developing on your Django project!

