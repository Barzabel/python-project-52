install:
	poetry install
	poetry lock

start_debug:
	poetry run python manage.py runserver



start:
	poetry run gunicorn -w 4 -b 0.0.0.0:8000 task_manager.wsgi:application

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