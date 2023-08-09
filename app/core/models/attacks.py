from django.db import models

class AttackType(models.TextChoices):
    INVALID = 'Invalid'
    UNPROVOKED = 'Unprovoked'
    PROVOKED = 'Provoked'
    SEA_DISASTER = 'Sea Disaster'

class SharkAttack(models.Model):
    date = models.DateField()
    type = models.CharField(max_length=10, choices=AttackType.choices, default=AttackType.INVALID)
    country = models.CharField(max_length=100)
    area = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    activity = models.CharField(max_length=100)
    victim_name = models.CharField(max_length=100)
    victim_gender = models.CharField(max_length=10)
    victim_age = models.SmallIntegerField()
    victim_injury = models.CharField(max_length=100)
    fatal = models.BooleanField(null=True, blank=True)
    time = models.CharField(max_length=100, null=True, blank=True)
    species = models.CharField(max_length=100, null=True, blank=True)
    source = models.CharField(max_length=100, null=True, blank=True)