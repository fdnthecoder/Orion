YAML_LINT = yamllint
API_DIR = API
TEXT_DIR = textorion
PYLINT = flake8
REQ_DIR = .

FORCE:

tests: FORCE
	$(PYLINT) *.py
	nosetests --exe --with-coverage --verbose --cover-package=Orion
	$(PYLINT) API/*.py
	nosetests --exe --with-coverage --verbose --cover-package=Orion/API

dev_env: FORCE
	pip3 install -r requirements-dev.txt
	pip3 install pymongo[srv]

prod: tests
	git add -A
	git commit -a
	git push origin main

%.py: FORCE
	nosetests tests.test_$* --nocapture

heroku-create:
	# install heroku:
	curl https://cli-assets.heroku.com/install.sh | sh
	heroku login
	# set up heroku app as remote for this repo
	heroku git:remote -a orion-crepe
	heroku config:set PYTHONPATH="/app"
	heroku config:set ORION_HOME="/app"
	echo "web: gunicorn --chdir API endpoints:app" > Procfile
	# enter deploy code in .travis.yml

heroku-run:
	heroku login
	git init
	heroku git:remote -a orion-crepe
	heroku config:set PYTHONPATH="/app"
	heroku config:set ORION_HOME="/app"
	echo "web: gunicorn --chdir API endpoints:app" > Procfile


