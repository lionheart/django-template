#!/bin/bash

# Update Filters
git config filter.sass.clean "sed '/^@media -sass-debug-info/ d'"
git config filter.sass.smudge cat

git config filter.css.clean "css-beautify --end_with_newline --file -"
git config filter.css.smudge cat

git config filter.js.clean "js-beautify --space-after-anon-function --brace-style=end-expand --preserve-newlines --end_with_newline --file -"
git config filter.js.smudge cat

git config filter.noop.clean cat
git config filter.noop.smudge cat

git config filter.xml.clean "xmllint --format -"
git config filter.xml.smudge cat

# Install hooks
cp git_config/hooks/post-checkout .git/hooks
cp git_config/hooks/pre-commit .git/hooks

if [ -f git_config/hooks/post-checkout-user ]; then
    cat git_config/hooks/post-checkout-user >> .git/hooks/post-checkout
fi
