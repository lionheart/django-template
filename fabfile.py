from fabric import colors
from fabric.api import *
from fabric.contrib.project import *

import git

env.app = '{{ project_name }}'
env.dest = "/var/www/%(app)s" % env
env.use_ssh_config = True

def reload_processes():
    sudo("kill -HUP `cat /tmp/%(app)s.pid`" % env)

def deploy():
    repo = git.Repo(".")
    sha = repo.head.commit.hexsha
    with cd(env.dest):
        run("git fetch --all")
        run("git checkout {} -f".format(sha))

    reload_processes()

def link_files():
    print(colors.yellow("Linking settings."))
    env.label = env.host_string.replace("%(app)s-", "")
    with cd(env.dest):
        sudo("rm -f local_settings.py")
        sudo("ln -s conf/settings/%(label)s.py local_settings.py" % env)

        sudo("rm -f conf/gunicorn/current.py")
        sudo("ln -s %(label)s.py conf/gunicorn/current.py" % env)

        sudo("rm -f conf/supervisor/current.ini")
        sudo("ln -s %(label)s.ini conf/supervisor/current.ini" % env)

        sudo("rm -f celeryconfig.py")
        sudo("ln -s conf/celery/%(label)s.py celeryconfig.py" % env)

        sudo("rm -f /etc/cron.d/%(label)s" % env)
        sudo("cp conf/cron/%(label)s.crontab /etc/cron.d/%(label)s" % env)

def reload_processes(reload_type="soft"):
    print(colors.yellow("Reloading processes."))

    env.label = env.host_string.replace("cmb-", "")
    with cd(env.dest):
        sudo("supervisorctl -c conf/supervisord.conf reread")
        sudo("supervisorctl -c conf/supervisord.conf update")
        # reload gunicorn

        sudo("kill -HUP `cat /tmp/gunicorn.%(app)s.%(label)s.pid`" % env)
        sudo("supervisorctl -c conf/supervisord.conf restart celery:*")

def add_commit_sha():
    repo = git.Repo(".")
    sha = repo.head.commit.hexsha
    sed("{}/settings.py".format(env.dest), "^COMMIT_SHA = .*$", 'COMMIT_SHA = "{}"'.format(sha), backup="\"\"", use_sudo=True)

