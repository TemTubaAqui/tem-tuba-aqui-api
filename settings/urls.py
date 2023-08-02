from django.contrib import admin
from django.urls import include, re_path

apps_urls = [
    re_path(r"^", include("app.core.urls")),
]

django_urls = [
    re_path(r"^admin/", admin.site.urls),
]

docs_urls = []

urlpatterns = apps_urls + django_urls + docs_urls
