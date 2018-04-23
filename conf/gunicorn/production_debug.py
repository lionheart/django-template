bind = "unix:/run/gunicorn/gunicorn.sock"

# http://gunicorn.org/design.html#how-many-workers
workers = 5

# Supervisor needs a non-daemonized process
daemon = False

pidfile = "/run/gunicorn/gunicorn.pid"
loglevel = "debug"
proc_name = "{{ project_name }}-debug"
worker_class = "gevent"
debug = True

django_settings = "{{ project_name }}.settings"

