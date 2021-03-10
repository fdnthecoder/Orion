YAML_LINT = yamllint
API_DIR = source
REQ_DIR = .

FORCE:

prod: tests github

tests: FORCE
	cd $(API_DIR); make tests

test_yaml:
	$(YAML_LINT) .travis.yml

github: FORCE
	- git commit -a
	git push origin master

dev_env: FORCE
	pip install -r $(REQ_DIR)/requirements-dev.txt

docs: FORCE
	cd $(API_DIR); make docs
