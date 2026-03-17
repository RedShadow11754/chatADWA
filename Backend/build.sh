#!/bin/bash
set -e

# Upgrade pip
pip install --upgrade pip

# Install dependencies
pip install -r Backend/requirements.txt

# Run migrations
python Backend/Project_Adwa/manage.py migrate --noinput

# Collect static files
python Backend/Project_Adwa/manage.py collectstatic --noinput
