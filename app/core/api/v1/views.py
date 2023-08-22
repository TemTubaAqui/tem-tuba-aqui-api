from django.db.models import Count, Max
from rest_framework import filters, mixins, viewsets

from app.core import models

from .serializers import BeachSerializer


class BeachViewSet(
    viewsets.GenericViewSet, mixins.ListModelMixin, mixins.RetrieveModelMixin
):
    serializer_class = BeachSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ("name", "country", "state", "city")

    def get_queryset(self):
        return (
            models.Beach.objects.order_by("country", "state", "city", "name")
            .prefetch_related("attacks")
            .annotate(attack_count=Count("attacks"), last_attack=Max("attacks__date"))
            .all()
        )
