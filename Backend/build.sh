#!/bin/bash
set -e

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r requirements.txt

# Run migrations
python Project_Adwa/manage.py migrate --noinput

# Collect static files
python Project_Adwa/manage.py collectstatic --noinput
