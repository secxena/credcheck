NAME := $(shell cat NAME)
VERSION := $(shell cat VERSION)

.PHONY: clean clean-pyc clean-build

clean: clean-pyc clean-build

clean-pyc:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +

clean-build:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/

setup:
	pipenv --python 3.7 install
	pipenv install '-e .'
	pipenv lock
	pipenv shell

build:
	python setup.py sdist bdist_wheel build
lint:
	flake8

test: clean-pyc
	python setup.py test

tox:
	#pyenv local `cat PY_VERSION`
	tox

install: clean
	pip install -r requirements.txt
	pip install -q -e .
	pip uninstall -y -q "${NAME}"

uninstall: clean
	pip freeze | xargs pip uninstall -y

pypicloud-push: clean
	pipenv run python setup.py sdist bdist_wheel upload -r pypicloud


push: pypicloud-push
	echo "Done"
