YAML_LINT = yamllint
API_DIR = API
TEXT_DIR = textorion
PYLINT = flake8
REQ_DIR = .

FORCE:

tests: FORCE
	$(PYLINT) *.py
	nosetests --exe --with-coverage --verbose --cover-package=Orion
dev_env: FORCE
	pip3 install -r requirements-dev.txt
prod: tests
	git commit -a
	git push origin main

%.py: FORCE
	nosetests tests.test_$* --nocapture
