#!/usr/bin/env bash
# Move into the Backend directory
cd Backend

# Run gunicorn from the folder where manage.py lives
exec gunicorn --chdir Project_Adwa Project_Adwa.wsgi:application \
  --bind 0.0.0.0:${PORT:-8000} \
  --log-level info
