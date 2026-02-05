web: python manage.py migrate && python create_admin.py && python manage.py collectstatic --noinput && gunicorn picdrop.wsgi:application --bind 0.0.0.0:$PORT --workers 3 --timeout 120
