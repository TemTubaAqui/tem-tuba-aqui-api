import os

from celery.utils.log import get_task_logger
from celery import Celery
from kombu import Exchange, Queue

logger = get_task_logger(__name__)

current_env = os.environ.get("ENVIRONMENT")
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings.settings")
app = Celery("settings")
app.config_from_object("django.conf:settings", namespace="CELERY")
app.autodiscover_tasks()

default_exchange = Exchange(f"temtubaaqui_{current_env}")

queue_name = f"temtubaaqui_{current_env}"
app.conf.task_queues = (
    Queue(
        queue_name,
        default_exchange,
        routing_key=f"temtubaaqui_default_{current_env}",
        queue_arguments={"x-queue-mode": "lazy"},
    ),
)
app.conf.task_routes = {"*": queue_name}
app.conf.task_default_queue = queue_name
