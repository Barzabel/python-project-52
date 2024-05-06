install:
	poetry install
	poetry lock

start_debug:
	poetry run python manage.py runserver

start:
	gunicorn task_manager.wsgi:application

test:
	poetry run coverage run --source='.' manage.py test

lint:
	poetry run flake8 task_manager

test-coverage-xml:
	poetry run coverage xml -o coverage.xml

show-test-coverage:
	poetry run coverage report

build:
	./build.sh