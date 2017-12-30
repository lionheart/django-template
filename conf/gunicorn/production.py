bind = "unix:/tmp/gunicorn.{{ project_name }}.production.sock"

# http://gunicorn.org/design.html#how-many-workers
workers = 5

# Supervisor needs a non-daemonized process, but is not Python 3 compatible. So
# until it is, we run as a daemon.
daemon = True

pidfile = "/tmp/gunicorn.{{ project_name }}.production.pid"
loglevel = "warning"
proc_name = "{{ project_name }}-production"
worker_class = "gevent"
debug = False

django_settings = "{{ project_name }}.settings"
