#!/bin/bash

PATH=$PATH:/usr/local/bin
DATE=`date +%Y%m%dT%H%M%S%z`

touch /tmp/upload_in_progress

YEAR=`date '+%Y'`
MONTH=`date '+%m'`
DAY=`date '+%d'`

# Create a new base backup every month and never delete archives.
if [ $DAY == 01 ]; then
    # Clear out the WAL directory.
    rm wal/*

    # Force creation of a WAL segment file.
    sudo -u postgres psql -c "SELECT pg_switch_xlog();"

    # Create a new base backup file.
    pg_basebackup -x -D wal/ -l {{  -w
fi

cd wal/

# Zip files with lrzip and bzip2 compression. For more information:
# http://ck.kolivas.org/apps/lrzip/README.benchmarks
ls | xargs lrzip -b

# Upload all compressed files to Amazon S3.
#   sudo apt-get install lrzip
ls *.lrz | xargs -I {} s3cmd put {} s3://backups-{{ project_name }}/$YEAR/$MONTH/

# Delete archives after uploading.
rm *

# Remove lockfile.
rm /tmp/upload_in_progress
