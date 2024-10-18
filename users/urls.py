from django.urls import path
from . import views


urlpatterns = [
    path("", views.get_users, name="get_users"),
    path("login/", views.login, name="login"),
    path("fetch_user/", views.fetch_user, name="fetch_user"),
]
