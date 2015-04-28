from fabric import colors
from fabric.api import *
from fabric.contrib.project import *
from fabric.contrib.files import sed, exists

import git

env.app = '{{ project_name }}'
env.dest = "/var/www/%(app)s" % env
env.use_ssh_config = True

def reload_processes():
    sudo("kill -HUP `cat /tmp/%(app)s.pid`" % env)

def sync():
    repo = git.Repo(".")
    sha = repo.head.commit.hexsha
    with cd(env.dest):
        run("git fetch --all")
        run("git checkout {} -f".format(sha))

    if "production" in env.host_string:
        with cd(env.dest):
            run("compass compile")

#            with prefix(". /home/ubuntu/environments/%(app)s/bin/activate" % env):
#                run("%(dest)s/manage.py syncmedia" % env)

def deploy():
    sync()
    link_files()
    reload_processes()
    add_commit_sha()

def link_files():
    print(colors.yellow("Linking settings."))
    env.label = env.host_string.replace("%(app)s-" % env, "")
    with cd(env.dest):
        sudo("rm -f local_settings.py")
        sudo("ln -s conf/settings/%(label)s.py local_settings.py" % env)

        sudo("rm -f conf/gunicorn/current.py")
        sudo("ln -s %(label)s.py conf/gunicorn/current.py" % env)

        sudo("rm -f celeryconfig.py")
        sudo("ln -s conf/settings/celery/%(label)s.py celeryconfig.py" % env)

        sudo("rm -f conf/supervisor/programs.ini" % env)
        sudo("ln -s %(label)s.ini conf/supervisor/programs.ini" % env)

def reload_processes(reload_type="soft"):
    print(colors.yellow("Reloading processes."))

    env.label = env.host_string.replace("%(app)s-" % env, "")
    with cd(env.dest):
        sudo("kill -HUP `cat /tmp/gunicorn.%(app)s.%(label)s.pid`" % env)

def add_commit_sha():
    repo = git.Repo(".")
    sha = repo.head.commit.hexsha
    sed("{}/settings.py".format(env.dest), "^COMMIT_SHA = .*$", 'COMMIT_SHA = "{}"'.format(sha), backup="\"\"", use_sudo=True)

