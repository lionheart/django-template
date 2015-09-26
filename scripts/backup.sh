#!/bin/bash

PATH=$PATH:/usr/local/bin
DATE=`date +%Y%m%dT%H%M%S%z`

sudo -u postgres pg_dump --no-privileges --no-owner --data-only {{ project_name }} > data.sql
sudo -u postgres pg_dump --no-privileges --no-owner --schema-only {{ project_name }} > schema.sql
tarsnap -cf $DATE data.sql schema.sql

# Read key not on server.
tarsnapper --target "\$date" --deltas 1h 1d 7d 30d 365d 18000d - expire
