# celery.py
import os
from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "hotelmanagement.settings")

app = Celery("hotelmanagement")
app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
