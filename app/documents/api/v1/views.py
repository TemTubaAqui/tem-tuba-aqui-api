from rest_framework import viewsets, permissions
from app.documents import models
from app.documents.api.v1 import serializers
from rest_framework.generics import get_object_or_404


class FileArtifactViewset(viewsets.ModelViewSet):
    serializer_classes = {
        "create": serializers.CreateFileArtifactSerializer,
        "update": serializers.UpdateFileArtifactSerializer,
        "partial_update": serializers.UpdateFileArtifactSerializer,
        "default": serializers.FileArtifactSerializer,
    }

    def get_permissions(self):
        classes = [permissions.DjangoModelPermissionsOrAnonReadOnly]
        if self.action in ["create", "update", "partial_update"]:
            classes.append(permissions.IsAuthenticated)

        return [permission() for permission in classes]

    def get_queryset(self):
        return models.FileArtifact.objects.all()

    def get_object(self) -> models.FileArtifact:
        obj = get_object_or_404(self.get_queryset(), name=self.kwargs["name"])
        self.check_object_permissions(self.request, obj)
        return obj

    def get_serializer_class(self):
        return self.serializer_classes.get(
            self.action,
            self.serializer_classes["default"],
        )

    def create(self, request, *args, **kwargs):
        request.data["name"] = self.kwargs["name"]
        return super().create(request, *args, **kwargs)
