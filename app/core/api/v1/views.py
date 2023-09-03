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

    def paginate_queryset(self, queryset):
        skip_pagination = self.request.query_params.get("skip_pagination", False)
        if skip_pagination:
            return None
        return super().paginate_queryset(queryset)

    def get_queryset(self):
        return (
            models.Beach.objects.order_by("country", "state", "city", "name")
            .prefetch_related("attacks")
            .annotate(attack_count=Count("attacks"), last_attack=Max("attacks__date"))
            .all()
        )
