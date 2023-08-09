from django.db import transaction

from app.core import models

class SharkService:

    @transaction.atomic
    def _fetch_data(self, request: models.SharkUpdateRequest):
        with request.run():
            # Do something
            pass

    def run(self, request_id: int):
        request = models.SharkUpdateRequest.objects.get(id=request_id)
        self._fetch_data(request)