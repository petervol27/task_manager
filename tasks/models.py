from django.db import models
from task_manager import settings


# Create your models here.
class Task(models.Model):
    name = models.CharField(max_length=255)
    deadline = models.DateField()
    done = models.BooleanField(default=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
