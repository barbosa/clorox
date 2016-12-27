install:
	sudo easy_install pip
	pip install -r requirements-dev.txt

test:
	nosetests

pypi_test:
	python setup.py sdist upload -r pypitest

pypi:
	python setup.py sdist upload -r pypi
