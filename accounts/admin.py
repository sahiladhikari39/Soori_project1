from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as DjangoUserAdmin

from .models import User


@admin.register(User)
class UserAdmin(DjangoUserAdmin):
    list_display = ("username", "email", "role", "client", "is_staff")
    fieldsets = DjangoUserAdmin.fieldsets + (
        ("Role & Tenant", {"fields": ("role", "client")}),
    )