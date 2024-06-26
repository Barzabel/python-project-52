install:
	poetry install
	poetry lock

start_debug:
	poetry run python manage.py runserver

migrate:
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate



start:
	poetry run gunicorn -w 4 -b 0.0.0.0:8000 task_manager.asgi:application -k uvicorn.workers.UvicornWorker

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