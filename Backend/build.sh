#!/bin/bash
set -e

# Install dependencies
pip install -r requirements.txt

# Apply migrations (from backend/project_adwa)
python project_adwa/manage.py migrate

# Collect static files
python project_adwa/manage.py collectstatic --noinput