from __future__ import absolute_import, unicode_literals
import os
from celery import Celery


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'OnlineConverter.settings')

app = Celery('youtube_converter', broker='redis://redis:6379/', backend='redis://redis:6379/')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
