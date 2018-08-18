import os
pythonpath = os.path.abspath("..")

bind = "0.0.0.0:{}".format(os.environ['PORT'])

# http://gunicorn.org/design.html#how-many-workers
workers = 3

# systemd needs a non-daemonized process
daemon = False

loglevel = "warning"
proc_name = "{{ project_name }}-production"
worker_class = "gevent"
debug = False

django_settings = "{{ project_name }}.settings"
