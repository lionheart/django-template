bind = "unix:/tmp/{{ project_name }}.sock"
workers = 3
daemon = False
pidfile = "/var/run/gunicorn/{{ project_name }}_debug.pid"
loglevel = "debug"
proc_name = "{{ project_name }}"
worker_class = "gevent"
debug = True
user = "gunicorn"
group = "gunicorn"

