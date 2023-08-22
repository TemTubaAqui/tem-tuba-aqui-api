from django.contrib import admin

from app.core import models
from app.shared.admin import BaseTaskAdmin

# Register your models here.

admin.site.register(models.BeachUpdateTask, BaseTaskAdmin)
admin.site.register(models.SharkUpdateTask, BaseTaskAdmin)


@admin.register(models.Beach)
class BeachAdmin(admin.ModelAdmin):
    list_display = ("name", "city", "state", "country")
    search_fields = ("name", "city", "state", "country")
    list_filter = ("state", "city", "country")


@admin.register(models.SharkAttack)
class SharkAttackAdmin(admin.ModelAdmin):
    list_display = (
        "beach",
        "date",
        "state",
        "country",
        "location",
        "type",
        "species",
        "victim_name",
    )
    search_fields = (
        "beach__name",
        "date",
        "state",
        "country",
        "location",
        "species",
        "victim_name",
    )
    list_filter = ("state", "country")
