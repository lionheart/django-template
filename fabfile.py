from fabric import colors
from fabric.api import *
from fabric.contrib.project import *

env.app = '{{ project_name }}'
env.dest = "/var/www/%(app)s" % env
env.use_ssh_config = True

def production():
    env.label = "production"

def reload_gunicorn():
    sudo("kill -HUP `cat /var/run/gunicorn/%(app)s.pid`" % env)

def start_gunicorn():
    with cd(env.dest):
        sudo("gunicorn_django -c gunicorn/%(label)s.py" % env)

def stop_gunicorn():
    sudo("kill `cat /var/run/gunicorn/%(app)s.pid`" % env)

def reload_nginx():
    print(colors.yellow("Reloading nginx"))
    sudo("kill -HUP `cat /var/run/nginx.pid`")

def shutdown_nginx():
    print(colors.red("Shutting down nginx"))
    sudo("kill -QUIT `cat /var/run/nginx.pid`")

def deploy():
    rsync()
    reload_gunicorn()

def rsync():
    print(colors.yellow("Deploying sources to %(host)s." % env))
    rsync_project(env.dest, ".", extra_opts="-FPOuhimrtyz")

