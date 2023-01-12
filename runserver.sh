#!/bin/sh
python manage.py collectstatic --no-input
gunicorn vuewe.wsgi --bind=0.0.0.0:80