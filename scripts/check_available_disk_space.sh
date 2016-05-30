#!/bin/bash

SPACE=`df -h /dev/xvda1 | tail -1 | awk '{ print $5 }' | sed 's/%//'`
if [ $SPACE -lt 90 ]; then
    echo "Space is running low."
fi

