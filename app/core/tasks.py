import logging
from settings.celery import app

from app.core.models import BeachUpdateTask
from app.core.services import BeachService

logger = logging.getLogger(__name__)

@app.task
def update_attacks_datase():
    ...

@app.task 
def run_beach_task(task_id: int):
    task = BeachUpdateTask.objects.filter(id=task_id).first()
    if task is None:
        logger.error(f"Task {task_id} not found")
        return
    
    BeachService().execute(task)

@app.task
def create_beach_task():
    BeachUpdateTask.objects.create()