#!/usr/bin/env bash

make install

python manage.py collectstatic --no-input
python manage.py migrate
