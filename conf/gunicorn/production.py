bind = "unix:/tmp/{{ project_name }}.sock"
workers = 3
daemon = True
pidfile = "/tmp/gunicorn.{{ project_name }}.production.pid"
loglevel = "error"
proc_name = "{{ project_name }}"
worker_class = "gevent"
debug = False
logfile = "/var/log/gunicorn/{{ project_name }}.log"
user = "gunicorn"
group = "gunicorn"

