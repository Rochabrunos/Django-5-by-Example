#!/bin/bash

cd /usr/src/app/
python manage.py makemigrations blog
python manage.py migrate 

# By default the password will be read from $DJANGO_SUPERUSER_PASSWORD environment variable
python manage.py createsuperuser --noinput --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL
python manage.py runserver 0.0.0.0:8000