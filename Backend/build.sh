#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Apply migrations
python Backend/Project_Adwa/manage.py migrate

# Collect static files
python Backend/Project_Adwa/manage.py collectstatic --noinput