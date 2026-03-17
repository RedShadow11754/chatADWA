#!/usr/bin/env bash
# Use environment port provided by Render (Render sets $PORT)
exec gunicorn project_adwa.wsgi:application \
  --bind 0.0.0.0:${PORT:-8000} \
  --workers 3 \
  --log-level info