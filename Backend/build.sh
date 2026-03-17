#!/bin/bash
set -e

pip install --upgrade pip
pip install -r requirements.txt

# Run migrations and collectstatic using the correct path to manage.py
python Project_Adwa/manage.py migrate --noinput
python Project_Adwa/manage.py collectstatic --noinput
