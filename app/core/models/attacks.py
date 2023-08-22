from django.db import models


class Beach(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        verbose_name_plural = "Beaches"

    def __str__(self) -> str:
        return f"{self.name} - {self.city}, {self.state}, {self.country}"

class AttackType(models.TextChoices):
    INVALID = "Invalid"
    UNPROVOKED = "Unprovoked"
    PROVOKED = "Provoked"
    SEA_DISASTER = "Sea Disaster"


class SharkAttack(models.Model):
    beach = models.ForeignKey(Beach, on_delete=models.CASCADE, null=True, blank=True, related_name="attacks")
    date = models.DateField(null=True, blank=True)
    type = models.CharField(choices=AttackType.choices, default=AttackType.INVALID)
    country = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    location = models.CharField(max_length=255, null=True, blank=True)
    activity = models.CharField(max_length=255, null=True, blank=True)
    victim_name = models.CharField(max_length=255, null=True, blank=True)
    victim_gender = models.CharField(max_length=10, null=True, blank=True)
    victim_age = models.SmallIntegerField(null=True, blank=True)
    victim_injury = models.CharField(max_length=255, null=True, blank=True)
    fatal = models.BooleanField(null=True, blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    species = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
