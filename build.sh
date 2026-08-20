#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --noinput
python manage.py migrate
2. Make build.sh Executable
If Git didn't track execute permissions for the script, Render will throw a Permission Denied error during deployment.

Run this in your local terminal, commit, and push:

Bash
chmod +x build.sh
git add build.sh
git commit -m "Make build.sh executable"
git push origin main