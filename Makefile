.PHONY: clean system-packages python-packages install tests run all
clean:
	find . -type f -name '*.pyc' -delete
	find . -type f -name '*.log' -delete

system-packages:
	sudo apt install python-pip -y

python-packages:
	pip install -r requirements.txt

install: system-packages python-packages

test:
	python -u manage.py test

init:
	python -u manage.py db init

mig:
	python -u manage.py db migrate

upg:
	python -u manage.py db upgrade

run:
	python -u manage.py init
	python -u manage.py run

coverage:
	coverage run --source app/api -m unittest discover -s app/test/

all: clean install tests run
