#!/usr/bin/env bash
# --chdir moves gunicorn into the folder where manage.py lives
exec gunicorn --chdir Project_Adwa Project_Adwa.wsgi:application \
  --bind 0.0.0.0:${PORT:-8000} \
  --workers 3 \
  --log-level info
