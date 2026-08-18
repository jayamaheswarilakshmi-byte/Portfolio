#!/usr/bin/env bash

pip install -r requirements.txt

python manage.py collectstatic --noinput

python manage.py migrate
python manage.py shell -c "import os; from django.contrib.auth import get_user_model; User = get_user_model(); username = os.environ.get('DJANGO_SUPERUSER_USERNAME', 'admin'); password = os.environ.get('DJANGO_SUPERUSER_PASSWORD'); user, created = User.objects.get_or_create(username=username); user.set_password(password); user.is_staff=True; user.is_superuser=True; user.save()"