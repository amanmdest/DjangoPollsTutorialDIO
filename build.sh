/#!/usr/bin/env bash
set -o errexit

# Modify this line as needed for you package manager (pip, poetry, etc.)
pip install poetry -U
poetry install --no-root

# Convert static asset files
python manage.py collectstatic --no-input

# Apply any outstanging database migrations
python manage.py migrate

# Create superuser
if [[ $CREATE_SUPERUSER ]]; then
    python manage.py createsuperuser --no-input
fi