.DEFAULT: help
.PHONY: help clean clean-pyc clean-build dist

help:
	@echo "clean: delete cached files"
	@echo "dist:  create distribution artifacts"

clean: clean-pyc clean-build

clean-pyc:
	@find . -name '*.pyc' -delete
	@find . -name '*.pyo' -delete
	@find . -name __pycache__ -delete

clean-build:
	@rm --force --recursive build dist *.egg-info


dist: clean
	python setup.py sdist bdist_wheel

