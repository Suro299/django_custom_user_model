from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("username", "email", "is_staff", "is_active", "avatar")
    list_filter = ("username", "email", "is_staff", "is_active", "avatar")
    fieldsets = (
        (None, {"fields": ("username", "email", "password", "avatar" )}),
        ("Permissions", {"fields": ("is_staff", "is_active", "groups", "user_permissions")}),
    )
    add_fieldsets = (
        (None, {
            "classes": ("wide",),
            "fields": (
                "username", "email", "password1", "password2", "is_staff",
                "is_active", "groups", "user_permissions", "avatar"
            )}
        ),
    )
    search_fields = ("email", "username")
    ordering = ("username", "is_staff")


admin.site.register(CustomUser, CustomUserAdmin)
