.PHONY: clean python-packages install tests run all

clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

python-packages:
	pip install -r requirements.txt

python-packages-dev:
	pip install -r requirements.txt -r requirements-dev.txt

tests:
	python manage.py test

all: clean python-packages tests
