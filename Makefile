USER := $(USER)

css:
	sass --update static/scss:static/css

setup-python:
	pip3 install -U pip
	pip3 install -r requirements.txt

setup-ruby:
	gem install bundler
	bundle install

setup-postgresql:
	-createuser -s $(USER)
	-createdb -O "$(USER)" "$(USER)"
	-bash scripts/database-init.sh

setup: setup-postgresql setup-python setup-ruby
	-ln -s conf/settings/local.py local_settings.py
	chmod +x manage.py
	python manage.py migrate

