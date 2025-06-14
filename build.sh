#!/usr/bin/env bash

# Exit if any command fails
set -o errexit

# Install dependencies
pip install -r requirements.txt

# Run Django commands
python manage.py collectstatic --noinput
python manage.py migrate
