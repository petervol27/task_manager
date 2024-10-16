from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task
from .serializers import TaskSerializer
from users.models import TaskUser


@api_view(["GET", "POST"])
def all_tasks(request):
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Succesfully added new task")
        else:
            return Response("Failed to add task")
    tasks = Task.objects.all()
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)


@api_view(["GET"])
def user_tasks(request, user_id):
    user = TaskUser.objects.get(id=user_id)
    tasks = Task.objects.filter(user=user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
