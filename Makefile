.PHONY: install lint test

install:
	pip install -r requirements.txt

lint:
	flake8 --ignore=E501

test:
	python -m unittest discover -v
	
format:
	autopep8 --in-place --aggressive --aggressive --recursive .

all: install lint format test