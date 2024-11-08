import logging
from contextlib import contextmanager

from django.db import models
from django.utils import timezone

logger = logging.getLogger(__name__)


class RequestStatus(models.TextChoices):
    PENDING = "PENDING"
    RUNNING = "RUNNING"
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"


class DateMixins(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Task(DateMixins):
    status = models.CharField(
        max_length=10, choices=RequestStatus.choices, default=RequestStatus.PENDING
    )
    message = models.JSONField(null=True, blank=True)
    error = models.JSONField(null=True, blank=True)

    running_at = models.DateTimeField(null=True, blank=True)
    success_at = models.DateTimeField(null=True, blank=True)
    failed_at = models.DateTimeField(null=True, blank=True)

    def transition_to_running(self):
        self.status = RequestStatus.RUNNING
        self.running_at = timezone.now()
        self.save()

    def transition_to_success(self, message=None):
        self.status = RequestStatus.SUCCESS
        self.success_at = timezone.now()
        self.message = message
        self.save()

    def transition_to_failed(self, error=None):
        self.status = RequestStatus.FAILED
        self.failed_at = timezone.now()
        self.error = error
        self.save()

    @contextmanager
    def run(self):
        logger.info(f"Running {self.__class__.__name__} {self.id}")
        self.transition_to_running()
        try:
            yield
        except Exception as e:
            logger.error(f"{self.__class__.__name__} {self.id} failed with error: {e}")
            error = {"error": str(e)}
            self.transition_to_failed(error=error)
            raise e
        else:
            logger.info(f"{self.__class__.__name__} {self.id} finished successfully")
            self.transition_to_success()
        finally:
            pass

    class Meta:
        abstract = True
