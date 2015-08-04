#!/bin/bash

CHANGED_JS_FILES=`git diff --cached --name-only | grep -E "^static/js/.*.js" | grep -v .min.js`

if [ -n "$CHANGED_JS_FILES" ]; then
    echo "Checking Javascript for the following files:"
    echo $CHANGED_JS_FILES

    if ! jscs $CHANGED_JS_FILES; then
        echo "Javascript issues detected; commit aborted."
        exit 1
    fi
fi

