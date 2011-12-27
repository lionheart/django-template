from fabric import colors
from fabric.api import *
from fabric.contrib.project import *

env.user = 'ubuntu'
env.app = 'goodiebag'
env.dest = "/var/www/%(app)s" % env

env.roledefs['app'] = ['web3.elmcitylabs.com']

def production():
    env.label = "production"

@roles('app')
def reload_gunicorn():
    sudo("kill -HUP `cat /var/run/gunicorn/%(app)s.pid`" % env)

@roles('app')
def start_gunicorn():
    with cd(env.dest):
        sudo("gunicorn_django -c gunicorn/%(label)s.py" % env)

@roles('app')
def stop_gunicorn():
    sudo("kill `cat /var/run/gunicorn/%(app)s.pid`" % env)

@roles('app')
def reload_nginx():
    print(colors.yellow("Reloading nginx"))
    sudo("kill -HUP `cat /var/run/nginx.pid`")

@roles('app')
def shutdown_nginx():
    print(colors.red("Shutting down nginx"))
    sudo("kill -QUIT `cat /var/run/nginx.pid`")

@roles('app')
def deploy():
    rsync()
    reload_gunicorn()

@roles('app')
def rsync():
    print(colors.yellow("Deploying sources to %(host)s." % env))
    key_string = " -i".join(env.key_filename)
    env.key_string = key_string
    local("""rsync --rsh='ssh -i %(key_string)s' -FPOuhimrtyz . %(user)s@%(host)s:%(dest)s""" % env)

