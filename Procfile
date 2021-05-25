web: python manage.py collectstatic --no-input; gunicorn QuizoBlast.wsgi --log-file - --log-level debug
web: gunicorn QuizoBlast.wsgi