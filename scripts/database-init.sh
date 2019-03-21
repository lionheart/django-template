#!/bin/bash

psql << EOF
CREATE ROLE {{ project_name }}_local WITH LOGIN ENCRYPTED PASSWORD '{{ project_name }}_local';
CREATE DATABASE {{ project_name }}_local WITH OWNER {{ project_name }}_local;
EOF

