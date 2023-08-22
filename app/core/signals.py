import logging
from typing import Type

from django.db import transaction
from django.db.models import signals
from django.dispatch import receiver

from app.core import tasks
from app.core.models import BeachUpdateTask

logger = logging.getLogger(__name__)


@receiver(signals.post_save, sender=BeachUpdateTask)
def run_beach_task(
    sender: Type[BeachUpdateTask], instance: BeachUpdateTask, created: bool, **kwargs
):
    def on_commit(instance: BeachUpdateTask):
        tasks.run_beach_task.delay(instance.id)

    if created:
        logger.info(f"Starting beach update task {instance.id}")
        transaction.on_commit(lambda: on_commit(instance))
