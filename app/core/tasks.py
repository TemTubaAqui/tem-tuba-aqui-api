import logging
from settings.celery import app

logger = logging.getLogger(__name__)

@app.task
def update_attacks_datase():
    ...