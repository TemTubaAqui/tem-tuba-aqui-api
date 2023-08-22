from django.urls import include, path
from rest_framework_nested import routers

from .views import BeachViewSet

beach_router = routers.DefaultRouter()
beach_router.register("beaches", BeachViewSet, "beaches")

urlpatterns = [path("", include(beach_router.urls))]
