For information on how to use this project template, check out the [wiki](https://github.com/lionheart/django-template/wiki/Django-1.11-Heroku).

# {{ project_name }}

### Table of Contents

* [Requirements](#requirements)
* [Local Setup](#local-setup)
* [Local Development](#local-development)
* [Deployment](#deployment)
* [Provisioning](#server-provisioning)

### Requirements


* [Homebrew](https://brew.sh) (not quite a "requirement" but recommended)

        $ /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"

* [Python 3](https://www.python.org/downloads/release/python-361/)

        $ brew install python3

* [pip](https://pip.pypa.io/en/stable/) (should come bundled when installing Python 3 via Homebrew)

* PostgreSQL

        $ brew install postgresql

    If you're in the mood for a longer read or have run into issues, here's a good [article](https://www.codefellows.org/blog/three-battle-tested-ways-to-install-postgresql) on how to install PostgreSQL on your system (covers Mac OS X, Windows, and Ubuntu).

## Local Development

1. Run the initialization script. This will set up your local Python virtual environment, install all requirements, link local settings, initialize the local development database, and run all migrations.

        $ ./scripts/init.sh

2. Set up the Git hooks (optional).

        $ git_config/configure.sh

3. Start the local development server and Sass.

        ({{ project_name }}) $ PYTHONUNBUFFERED=True foreman start -f Procfile.dev

Map "local.{{ project_name }}.com" to 127.0.0.0 using DNS. If you haven't yet registered a domain, add the following line to your `/etc/hosts` file.

    127.0.0.1 local.{{ project_name }}.com

After you've done that, open your browser and navigate to "[local.{{ project_name }}.com](http://local.{{ project_name }}.com)". Your project is now running!

Heroku Setup
------------

1. Create the project on [Heroku](https://heroku.com) or connect it to an existing project.

       heroku git:remote -a HEROKU-PROJECT-NAME

   Or:

       heroku create

2. Add the PostgreSQL addon.

       heroku addons:create heroku-postgresql

3. Specify that the project uses the Python buildpack.

       heroku buildpacks:set heroku/python

4. Set the environment variables.

       heroku config:set APP_ENVIRONMENT=production
       heroku config:set AWS_ACCESS_KEY_ID=XXX
       heroku config:set AWS_SECRET_ACCESS_KEY=XXX
       heroku config:set AWS_STORAGE_BUCKET_NAME=XXX

Deployment
----------

1. Push to Heroku.

       git push heroku master

2. Sync static files to S3.

       heroku run python manage.py syncmedia

PostgreSQL Installation
-----------------------

If you're on a Mac and have [Homebrew](https://github.com/homebrew/homebrew) installed, we'll keep it simple.

    brew install postgresql

If you're in the mood for a longer read or have run into issues, here's a good [article](https://www.codefellows.org/blog/three-battle-tested-ways-to-install-postgresql) on how to install PostgreSQL on your system (covers Mac OS X, Windows, and Ubuntu).
