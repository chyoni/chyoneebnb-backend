from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    list_display = ("id", "username", "nickname", "email", "is_host", "is_superuser")

    fieldsets = (
        (
            "Profile",
            {
                "fields": (
                    "username",
                    "nickname",
                    "avatar",
                    "password",
                    "email",
                    "bio",
                    "phone",
                    "location",
                    "currency",
                    "language",
                    "gender",
                )
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        ("Important dates", {"fields": ("last_login", "date_joined")}),
    )
