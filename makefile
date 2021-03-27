PYLINT = flake8

FORCE:

tests: FORCE
	$(PYLINT) *.py
	nosetests --exe --with-coverage --verbose --cover-package=TakeOff
dev_env: FORCE
	echo "installing requirements"
prod: tests
	git commit -a
	git push origin main

%.py: FORCE
	nosetests tests.test_$* --nocapture
