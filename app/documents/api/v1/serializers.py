from rest_framework import serializers

from app.documents import models


class CreateFileArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FileArtifact
        fields = "__all__"
        read_only_fields = ("id",)

class UpdateFileArtifactSerializer(serializers.ModelSerializer):
    class  Meta:
        model = models.FileArtifact
        fields = ("file",)

class FileArtifactSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FileArtifact
        fields = "__all__"
        read_only_fields = (
            "id",
            "name",
            "file",
        )
