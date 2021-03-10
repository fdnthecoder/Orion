LINTER = flake8
DOCFILES = $(shell ls *.py | sed 's/.py/.html/')

FORCE:

docs: $(DOCFILES)

%.html: %.py
	pydoc3 -w ./$<
	git add $@

tests: lint unit

unit: FORCE
	python3 -m unittest tests.test_endpoints

lint: FORCE
	$(LINTER) *.py
