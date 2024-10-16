from django.contrib import admin
from .models import TaskUser

# Register your models here.


class TaskAdmin(admin.ModelAdmin):
    list_display = ("username", "fav_color", "phone")


admin.site.register(TaskUser, TaskAdmin)
