YAML_LINT = yamllint
SRC_DIR = source
REQ_DIR = requirements

FORCE:

prod: tests github

tests: test_yaml
	cd source; make tests

test_yaml:
	$(YAML_LINT) .travis.yml

github: FORCE
	- git commit -a
	git push origin master

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt

docs: FORCE
	cd source; make docs
