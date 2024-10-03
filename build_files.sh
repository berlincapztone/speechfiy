#!/bin/bash
# Install dependencies
pip install -r requirements.txt

# Run Django's collectstatic command to gather static files
python manage.py collectstatic --noinput
