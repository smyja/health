#!/bin/sh
python manage.py collectstatic --no-input
gunicorn beep.wsgi --bind=0.0.0.0:80