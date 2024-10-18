from .models import TaskUser
from rest_framework import serializers


class TaskUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = TaskUser
        fields = "__all__"
