#!/usr/bin/env bash

# http://www.philchen.com/2015/08/08/how-to-make-a-scalable-python-web-app-using-flask-and-gunicorn-nginx-on-ubuntu-14-04

if [[ -z ${APP_IP} ]]; then APP_IP=0.0.0.0; echo ''; fi
if [[ -z ${APP_PORT} ]]; then APP_PORT=8000; echo ''; fi
if [[ -z ${APP_NAME} ]]; then APP_NAME=models-serving-app; echo ''; fi
if [[ -z ${APP_GUNICORN_WORKERS} ]]; then APP_GUNICORN_WORKERS=3; echo ''; fi
if [[ -z ${APP_GUNICORN_TIMEOUT} ]]; then APP_GUNICORN_TIMEOUT=120; echo ''; fi
if [[ -z ${GUNICORN_LOG_LEVEL} ]]; then GUNICORN_LOG_LEVEL=INFO; echo ''; fi

echo 'starting gunicorn using params:'
echo 'app endpoint: ' $APP_IP':'$APP_PORT
echo 'app name: ' $APP_NAME
echo 'workers num: ' $APP_GUNICORN_WORKERS
echo 'timeout: ' $APP_GUNICORN_TIMEOUT

gunicorn --name $APP_NAME \
    -w $APP_GUNICORN_WORKERS \
    -b $APP_IP:$APP_PORT \
    --timeout $APP_GUNICORN_TIMEOUT \
    --log-level $GUNICORN_LOG_LEVEL \
    app.main:flask_app
