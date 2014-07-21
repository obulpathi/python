.PHONY: build test upload install

build:
	python setup.py sdist
	python setup.py bdist_wheel

register:
	python setup.py register -r test

upload:
	python setup.py sdist upload -r test
	python setup.py bdist_wheel upload -r test

install:
	pip install -i https://testpypi.python.org/pypi mypackage

clean:
	rm -rf *.pyc
	rm -rf build/
	rm -rf dist/
	rm -rf mypackage.egg-info/
