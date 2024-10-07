#!/bin/bash

# Update and install Python and pip if not present
if ! command -v python3 &> /dev/null
then
    echo "Python not found, installing Python"
    apt-get update
    apt-get install -y python3 python3-pip
fi

# Install pip packages from requirements.txt
pip3 install -r requirements.txt

# Run Django commands
python3 manage.py collectstatic --noinput
python3 manage.py migrate
