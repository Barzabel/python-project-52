#!/usr/bin/env bash


#rm -rf `find . -type d -name  migrations`

make install

poetry run python manage.py collectstatic --no-input

#poetry run python manage.py sqlflush | poetry run python manage.py dbshell


poetry run python manage.py migrate


# if [[ $CREATE_SUPERUSER ]];
# then
#   poetry run python manage.py createsuperuser --no-input
# fi