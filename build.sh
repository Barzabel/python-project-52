#!/usr/bin/env bash

make install

poetry run python manage.py collectstatic --no-input
poetry run python manage.py migrate
