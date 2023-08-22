from django.db import transaction

from app.core.models import SharkUpdateTask


class SharkService:
    @transaction.atomic
    def _run(self, request: SharkUpdateTask):
        with request.run():
            # Do something
            pass

    def execute(self, task: SharkUpdateTask):
        self._run(task)
