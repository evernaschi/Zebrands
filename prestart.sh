#! /usr/bin/env bash

# Check if initialization has already been performed
if [ -f /code/app/.initialized ]; then
  echo "Initialization has already been performed, skipping."
  exit 0
fi

echo "Performing initialization..."

# Let the DB start
python -m app.backend_pre_start

# Create initial data in DB
python -m app.initial_data

# Create flag file to indicate that initialization has been performed
touch /code/app/.initialized

echo "Initialization completed."