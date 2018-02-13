bind = "unix:/tmp/gunicorn.{{ project_name }}.production.sock"

# http://gunicorn.org/design.html#how-many-workers
workers = 5

# systemd needs a non-daemonized process
daemon = False

pidfile = "/var/run/gunicorn.pid"
loglevel = "warning"
proc_name = "{{ project_name }}-production"
worker_class = "gevent"
debug = False

django_settings = "{{ project_name }}.settings"
