import os

from celery import Celery

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "project_site.settings")

app = Celery("project_site")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()
