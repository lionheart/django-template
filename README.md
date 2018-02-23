![](meta/repo-banner.png)
[![](meta/repo-banner-bottom.png)][lionheart-url]

For information on how to use this project template, check out the [wiki](https://github.com/lionheart/django-template/wiki/Django-2.0).

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

        ({{ project_name }}) $ foreman start -f Procfile.dev

    Map "local.{{ project_name }}.com" to 127.0.0.0 using DNS. If you haven't yet registered a domain, add the following line to your `/etc/hosts` file.

        127.0.0.1 local.{{ project_name }}.com

    After you've done that, open your browser and navigate to "[local.{{ project_name }}.com](http://local.{{ project_name }}.com)". Your project is now running!

## Deployment

1. Add the following to your SSH configuration in `.ssh/config` (create it if it doesn't already exist).

        Host {{ project_name }}-production
          HostName IP_ADDRESS_HERE
          IdentityFile ~/.ssh/{{ project_name }}-web-servers.pem
          User ubuntu

3. Acquire the SSH private key for the {{ project_name }} production server and move it to the path referenced above (`~/.ssh/{{ project_name }}-web-servers.pem`). Make sure permissions are set to 400.

        $ cd ~/.ssh
        $ chmod 400 {{ project_name }}-web-servers.pem

2. Make sure all of your local changes are pushed to GitHub.

3. In the project root, run the following to deploy to the server. Make sure you're running in the virtual environment as specified in step 2 of the prerequisites.

        ({{ project_name }}) $ fab -H {{ project_name }}-production deploy

## Server Provisioning

1. Log into the server.

        $ ssh {{ project_name }}-production

2. Run the provisioning script.

        curl REMOTE_PATH_TO_PROVISIONING_SCRIPT | sudo sh ENVIRONMENT=production sh

3. Update the hostname by editing `/etc/hostname` and `/etc/hosts`.

4. Generate an SSH private key and add it as a deploy key to whatever code host you are using..

        ssh-keygen

5. Clone the repo to `/var/www/{{ project_name }}`.

        cd /var/www/{{ project_name }}
        git clone REPO_URL .

6. Update requirements.

        . /home/ubuntu/environments/{{ project_name }}/bin/activate
        pip install -r requirements.txt

7. Start gunicorn.

        /home/ubuntu/environments/{{ project_name }}/bin/gunicorn wsgi:application -c /var/www/{{ project_name }}/conf/gunicorn/current.py

8. Restart nginx.

[lionheart-url]: https://lionheartsw.com/

