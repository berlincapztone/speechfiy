#!/bin/bash

# Check for Python installation
if ! command -v python &> /dev/null
then
    echo "Python not found. Please install Python and pip manually."
    exit 1
fi

# Install pip packages
pip install -r requirements.txt

# Run Django commands
python manage.py collectstatic --noinput
python manage.py migrate  # Optional: Add if you need to run migrations
