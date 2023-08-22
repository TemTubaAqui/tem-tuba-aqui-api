from rest_framework import serializers

from app.core import models


class BeachSerializer(serializers.ModelSerializer):
    attack_count = serializers.IntegerField()
    last_attack = serializers.DateField()

    class Meta:
        model = models.Beach
        fields = "__all__"
