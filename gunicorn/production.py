bind = "unix:/tmp/goodiebag.sock"
workers = 3
daemon = True
pidfile = "/var/run/gunicorn/goodiebag.pid"
loglevel = "error"
proc_name = "goodiebag"
worker_class = "gevent"
debug = False
logfile = "/var/log/gunicorn/goodiebag.log"
user = "gunicorn"
group = "gunicorn"

