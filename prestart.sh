#!/usr/bin/env bash


# Exit immediately if any command fails
set -e

# Let the DB start
echo "Running backend pre-start script..."
python ./app/backend_pre_start.py

# Run migrations
echo "Running Alembic migrations..."
alembic upgrade head

# Create initial data in DB
echo "Running initial data setup..."
python ./app/initial_data.py
