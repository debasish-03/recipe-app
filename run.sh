#!/bin/bash

export APP_MODULE=${APP_MODULE-app.main:app}
export HOST=${HOST:-127.0.0.1}   # Set HOST to 127.0.0.1
export PORT=${PORT:-8001}

echo "Running Uvicorn on $HOST:$PORT with APP_MODULE=$APP_MODULE"
exec uvicorn --reload --host $HOST --port $PORT "$APP_MODULE"

# poetry run bash ./run.sh
