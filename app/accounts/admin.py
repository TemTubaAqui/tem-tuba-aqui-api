from django.contrib import admin
from django.contrib.auth.forms import AdminPasswordChangeForm

from app.accounts.models import User

# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("id", "email", "is_staff", "is_active", "date_joined")
    list_filter = ("is_staff", "is_active")
    search_fields = ("email", "id")
    filter_horizontal = ("groups", "user_permissions")

    change_password_form = AdminPasswordChangeForm