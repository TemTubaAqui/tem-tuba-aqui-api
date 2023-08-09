from app.core.models import management

from rest_framework import generics, views, response
from rest_framework.generics import get_object_or_404

class TestView(views.APIView):
    def get(self, request, *args, **kwargs):
        return response.Response({'hello': 'world'})