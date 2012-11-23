Paste the following URL into your browser and download it to a writable directory:

    https://bitbucket.org/aurorasoftware/django-bootstrap/get/django-1.4.tar.bz2

Afterwards, just run the following:

    django-admin.py startproject -e md -e ngx --template=django-1.4.tar.bz2 project_name

After cloning, just run the following:

Getting Started
===============

Before doing any of this, you'll need to install Python and pip.

    $ pip install virtualenv
    $ virtualenv .
    ({{ project_name }}) $ pip install -r requirements.txt
    # wait for a couple of minutes, hopefully nothing goes wrong!
    ({{ project_name }}) $ ln -s conf/settings/local.py local_settings.py
    ({{ project_name }}) $ ./manage.py syncdb
    ({{ project_name }}) $ sudo ./manage.py runserver
    Validating models...
    0 errors found

    Django version 1.4.2, using settings '{{ project_name }}.settings'
    Running django-devserver 0.3.1
    Threaded django server is running at http://0.0.0.0:80/
    Quit the server with CONTROL-C.

Open your browser, navigate to "http://local.{{ project_name }}.com", and enjoy!

