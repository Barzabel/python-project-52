#!/usr/bin/env bash

make install

poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate users zero --fake
poetry run python manage.py makemigrations
poetry run python manage.py migrate

# if [[ $CREATE_SUPERUSER ]];
# then
#   poetry run python manage.py createsuperuser --no-input
# fi