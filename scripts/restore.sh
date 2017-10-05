#!/bin/bash

if [[ -z "$1" ]]; then
    echo "Please provide an archive name from the list below. Please wait."
    tarsnap --list-archives --keyfile ~/.tarsnap/{{ project_name }}-tarsnap.key | sort
    exit
fi

if [ -e $1/schema.sql ]; then
    echo "Archive already downloaded. Using cached copy."
else
    mkdir $1
    tarsnap -x --keyfile ~/.tarsnap/{{ project_name }}-tarsnap.key -f $1 -C $1
fi

dropdb {{ project_name }}_local
createdb {{ project_name }}_local -O {{ project_name }}_local
export PGOPTIONS='--client-min-messages=warning'
psql --pset pager=off --quiet -U {{ project_name }}_local {{ project_name }}_local < $1/schema.sql
psql --pset pager=off --quiet -U {{ project_name }}_local {{ project_name }}_local < $1/data.sql

