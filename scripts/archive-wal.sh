#!/bin/bash

# USAGE:
#
# In postgresql.conf
#   archive_command = 'your_scripts_directory/archive-wal.sh %p %f'
#

SOURCE=$1
FILENAME=$2

if [ -f /tmp/upload_in_progress ]; then
    exit 1
fi

if [ -f "/home/ubuntu/wal/$FILENAME" ]; then
    exit 1
fi

cp $SOURCE "/home/ubuntu/wal/$FILENAME"

