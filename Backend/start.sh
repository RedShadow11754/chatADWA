#!/usr/bin/env bash
exec gunicorn --chdir Project_Adwa Project_Adwa.wsgi:application \
  --bind 0.0.0.0:${PORT:-8000} \
  --log-level info
