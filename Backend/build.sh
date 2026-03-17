#!/bin/bash
set -e

# Make sure pip is updated (optional)
pip install --upgrade pip

# Install dependencies
pip install -r Backend/requirements.txt

# Apply migrations
python Backend/Project_Adwa/manage.py migrate

# Collect static files
python Backend/Project_Adwa/manage.py collectstatic --noinput