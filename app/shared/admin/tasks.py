from django.contrib import admin


class BaseTaskAdmin(admin.ModelAdmin):
    list_display = ("status", "created_at", "updated_at")
    list_filter = ("status", "created_at", "updated_at")
    search_fields = ("status",)
    readonly_fields = ("created_at", "updated_at")
    ordering = ("created_at", "updated_at", "status")