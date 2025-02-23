from celery import shared_task


@shared_task
def update_appeals_task():
    print("Task started")
