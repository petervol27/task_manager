from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_users, name="get_users"),
    path("register/", views.register, name="register"),
]
