bind = "unix:/tmp/{{ project_name }}.sock"
workers = 3
daemon = False
pidfile = "/tmp/gunicorn.{{ project_name }}.production.pid"
loglevel = "debug"
proc_name = "{{ project_name }}"
worker_class = "gevent"
debug = True
user = "gunicorn"
group = "gunicorn"

