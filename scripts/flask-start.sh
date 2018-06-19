#!/usr/bin/env bash

if [[ -z ${APP_PORT} ]]; then APP_PORT=8000; fi

echo 'starting flask using port: ' $APP_PORT
python -m app.main --port=$APP_PORT
