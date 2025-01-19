#!/bin/bash
# Install WhiteNoise
pip install -r requirements.txt

# Create staticfiles directory if it doesn't exist
mkdir -p staticfiles

# Collect static files
python manage.py collectstatic --noinput

echo "Static files have been collected and WhiteNoise has been installed."
echo "Please restart your application for changes to take effect."