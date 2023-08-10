from django.urls import path

from app.documents.api.v1 import views

urlpatterns = [
    path(
        "files/<str:name>/",
        views.FileArtifactViewset.as_view(
            {
                "get": "retrieve",
                "post": "create",
                "put": "update",
                "patch": "partial_update",
                "delete": "destroy",
            }
        ),
    ),
    path(
        "files/",
        views.FileArtifactViewset.as_view({"get": "list"}),
    ),
]
