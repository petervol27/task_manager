from django.contrib import admin
from .models import TaskUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = TaskUser
    fieldsets = UserAdmin.fieldsets + ((None, {"fields": ("fav_color", "phone")}),)
    add_fieldsets = UserAdmin.add_fieldsets + (
        (
            None,
            {"fields": ("fav_color", "phone")},
        ),
    )
    list_display = ["username", "fav_color", "phone"]


admin.site.register(TaskUser, CustomUserAdmin)
