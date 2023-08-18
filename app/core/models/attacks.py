from django.db import models


class Beach(models.Model):
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    beach = models.CharField(max_length=255)
    latitude = models.FloatField()
    longitude = models.FloatField()


class AttackType(models.TextChoices):
    INVALID = "Invalid"
    UNPROVOKED = "Unprovoked"
    PROVOKED = "Provoked"
    SEA_DISASTER = "Sea Disaster"


class SharkAttack(models.Model):
    date = models.DateField()
    type = models.CharField(choices=AttackType.choices, default=AttackType.INVALID)
    country = models.CharField(max_length=255)
    area = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    activity = models.CharField(max_length=255)
    victim_name = models.CharField(max_length=255)
    victim_gender = models.CharField(max_length=10)
    victim_age = models.SmallIntegerField()
    victim_injury = models.CharField(max_length=255)
    fatal = models.BooleanField(null=True, blank=True)
    time = models.CharField(max_length=255, null=True, blank=True)
    species = models.CharField(max_length=255, null=True, blank=True)
    source = models.CharField(max_length=255, null=True, blank=True)
