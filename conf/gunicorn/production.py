bind = "unix:/tmp/gunicorn.{{ project_name }}.production.sock"

# http://gunicorn.org/design.html#how-many-workers
workers = 5

# Supervisor needs a non-daemonized process
daemon = False

pidfile = "/tmp/gunicorn.{{ project_name }}.production.pid"
loglevel = "warning"
proc_name = "{{ project_name }}-production"
worker_class = "gevent"
debug = False

