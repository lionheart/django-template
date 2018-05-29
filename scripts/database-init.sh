#!/bin/bash

psql << EOF
CREATE ROLE bonnie_local WITH LOGIN ENCRYPTED PASSWORD 'bonnie_local';
CREATE DATABASE bonnie_local WITH OWNER bonnie_local;
EOF

