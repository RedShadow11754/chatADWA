#!/usr/bin/env bash
set -e

# install deps
pip install --upgrade pip
pip install -r requirements.txt

# run migrations & collectstatic (uses env vars on Render)
python manage.py migrate --noinput
python manage.py collectstatic --noinput