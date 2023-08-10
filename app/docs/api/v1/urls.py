from django.urls import re_path

from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularSwaggerView,
    SpectacularRedocView,
)

urlpatterns = [
    re_path(r"^schema/", SpectacularAPIView.as_view(), name="schema"),
    re_path(
        r"^swagger/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    re_path(r"^redoc/", SpectacularRedocView.as_view(url_name="schema"), name="redoc"),
]
