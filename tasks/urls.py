from django.urls import path
from . import views

urlpatterns = [
    path("", views.all_tasks, name="All tasks"),
    path("<int:user_id>", views.user_tasks, name="User tasks"),
]
