bind = "unix:/tmp/goodiebag.sock"
workers = 3
daemon = False
pidfile = "/var/run/gunicorn/goodiebag_debug.pid"
loglevel = "debug"
proc_name = "goodiebag"
worker_class = "gevent"
debug = True
user = "gunicorn"
group = "gunicorn"

