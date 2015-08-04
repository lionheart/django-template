#!/bin/bash

CHANGED_PYTHON_FILES=`git diff --cached --name-only | grep py$`

if [ -n "$CHANGED_PYTHON_FILES" ]; then
    CHANGED_FILES=`echo $CHANGED_PYTHON_FILES | tr '\n ' ,`

    if ! [ -z "echo $CHANGED_FILES | sed -e 's/^[ \t]*//'" ]; then
        echo "Checking PEP-8 Compliance for the following files:"
        printf "$CHANGED_PYTHON_FILES\n"
        if ! pep8 --filename=$CHANGED_FILES; then
            echo "PEP-8 errors detected; commit aborted."
            exit 1
        fi
    fi
fi

