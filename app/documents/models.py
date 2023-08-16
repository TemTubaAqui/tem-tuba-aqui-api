from django.db import models


class FileArtifact(models.Model):
    name = models.CharField(max_length=255, unique=True)
    file = models.FileField(upload_to="documents/artifacts/%Y/%m/%d")

    def __str__(self):
        return self.name
