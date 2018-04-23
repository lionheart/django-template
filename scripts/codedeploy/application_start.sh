#!/usr/bin/env bash

systemctl stop gunicorn.service
systemctl restart gunicorn.socket
service cron restart

