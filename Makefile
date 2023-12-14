.PHONY: install lint test

install:
	pip install -r requirements.txt

lint:
	flake8 --ignore=E501

test:
	pytest -vv

all: install lint test