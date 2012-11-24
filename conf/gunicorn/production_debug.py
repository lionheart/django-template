import os
pythonpath = os.path.abspath("..")

bind = "unix:/tmp/gunicorn.{{ project_name }}.production.sock"

# http://gunicorn.org/design.html#how-many-workers
workers = 5

# Supervisor needs a non-daemonized process
daemon = False

pidfile = "/tmp/gunicorn.{{ project_name }}.production.pid"
loglevel = "debug"
proc_name = "{{ project_name }}-debug"
worker_class = "gevent"
debug = True

django_settings = "{{ project_name }}.settings"

