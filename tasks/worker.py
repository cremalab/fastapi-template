from celery import Celery

from config import settings

worker = Celery(
    settings.App.name, broker=settings.Celery.broker, backend=settings.Celery.backend
)


class Tasks:
    example_task = "example_task"
