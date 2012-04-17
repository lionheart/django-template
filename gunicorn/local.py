bind = "unix:/tmp/{{ project_name }}.sock"
workers = 3
daemon = False
pidfile = "/tmp/{{ project_name }}.pid"
loglevel = "debug"
proc_name = "{{ project_name }}"
worker_class = "gevent"
debug = True

