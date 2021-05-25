web: gunicorn QuizoBlast.wsgi
web: python manage.py collectstatic --no-input; gunicorn QuizoBlast.wsgi --log-file - --log-level debug