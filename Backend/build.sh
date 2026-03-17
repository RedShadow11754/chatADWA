#!/usr/bin/env bash
# exit on error
set -o errexit

# Move into the Backend directory where requirements.txt lives
cd Backend

pip install --upgrade pip
pip install -r requirements.txt

# Run migrations and collectstatic using the path to manage.py
python Project_Adwa/manage.py migrate --noinput
python Project_Adwa/manage.py collectstatic --noinput
