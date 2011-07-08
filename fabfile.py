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
    migrate_db()
    reload_gunicorn()

@roles('app')
def rsync():
    print(colors.yellow("Deploying sources to %(host)s." % env))
    local("""rsync --exclude-from=RSYNC_EXCLUDES -POuhimrtyz --delete-after --delete-excluded . %(user)s@%(host)s:%(dest)s""" % env)

@roles('app')
def migrate_db():
    with cd(env.dest):
        run("./manage.py migrate app")


