.DEFAULT: help
.PHONY: help clean clean-pyc clean-build dist test test-coverage

help:
	@echo "clean         : delete cached files"
	@echo "clean-pyc     : delete *.py{c,o} & __pycache__ files"
	@echo "clean-build   : delete distribution artifacts"
	@echo "dist          : create distribution artifacts"
	@echo "test          : run tests"
	@echo "test-coverage : run tests (with coverage)"

clean: clean-pyc clean-build

clean-pyc:
	@find . -name '*.pyc' -delete
	@find . -name '*.pyo' -delete
	@find . -name __pycache__ -delete

clean-build:
	@rm --force --recursive build dist *.egg-info


dist: clean
	python setup.py sdist bdist_wheel

test:
	python setup.py nosetests

test-coverage:
	python setup.py nosetests --with-coverage --cover-package=discogs_api
