#!/usr/bin/env bash


#rm -rf `find . -type d -name  migrations`

make install

poetry run python manage.py collectstatic --no-input

#poetry run python manage.py sqlflush | poetry run python manage.py dbshell



poetry run python manage.py makemigrations 
poetry run python manage.py makemigrations users
poetry run python manage.py makemigrations status
poetry run python manage.py makemigrations labels
poetry run python manage.py makemigrations tasks
poetry run python manage.py migrate --run-syncdb


# if [[ $CREATE_SUPERUSER ]];
# then
#   poetry run python manage.py createsuperuser --no-input
# fi