from django.db import models
from django.contrib.auth.models import AbstractUser


class TaskUser(AbstractUser):
    fav_color = models.CharField(max_length=30)
    phone = models.CharField(max_length=255)
