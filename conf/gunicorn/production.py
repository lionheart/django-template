bind = "unix:/run/gunicorn/gunicorn.sock"

# http://gunicorn.org/design.html#how-many-workers
workers = 5

# systemd needs a non-daemonized process
daemon = False

pidfile = "/run/gunicorn/gunicorn.pid"
loglevel = "warning"
proc_name = "{{ project_name }}-production"
worker_class = "gevent"
debug = False

django_settings = "{{ project_name }}.settings"
