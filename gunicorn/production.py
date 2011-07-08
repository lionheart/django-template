bind = "unix:/tmp/blah.sock"
workers = 3
daemon = True
pidfile = "/var/run/gunicorn/blah.pid"
loglevel = "error"
proc_name = "blah"
worker_class = "gevent"
debug = False
logfile = "/var/log/gunicorn/blah.log"
user = "gunicorn"
group = "gunicorn"

