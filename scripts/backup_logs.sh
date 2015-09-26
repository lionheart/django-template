#!/bin/bash

PATH=$PATH:/usr/local/bin

mv /var/log/*.bz2 /var/log/rotated
ls /var/log/*/*.bz2 | grep -v ^/var/log/rotated/ | xargs -I {} mv {} /var/log/rotated
mv /var/log/*.gz /var/log/rotated

for LOG_FILENAME in `ls /var/log/rotated/*`
do
    if [ -f $LOG_FILENAME ]; then
        if s3cmd put $LOG_FILENAME s3://logs-{{ project_name }}/`date +%Y/%m/%d`/; then
            rm $LOG_FILENAME
        fi
    fi
done

