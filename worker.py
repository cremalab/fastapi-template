from celery.schedules import crontab

from tasks.worker import Tasks, worker

worker.autodiscover_tasks(["tasks"], force=True)


worker.conf.beat_schedule = {
    "example_task": {
        "task": Tasks.example_task,
        "schedule": crontab(),
    },
}
