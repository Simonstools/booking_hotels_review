#!/bin/sh

. ../.venv/bin/activate

echo "Applying migrations"
python manage.py migrate --noinput

echo "Starting Django app..."
exec "$@"
