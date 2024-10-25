from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .models import Task
from .serializers import TaskSerializer
from users.models import TaskUser


@api_view(["GET", "POST"])
@permission_classes([IsAuthenticated])
def tasks(request):
    if request.method == "POST":
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Succesfully added new task")
        else:
            return Response("Failed to add task")
    if request.user.is_staff:
        tasks = Task.objects.all()
    else:
        tasks = Task.objects.filter(user=request.user)
    serializer = TaskSerializer(tasks, many=True)
    return Response(serializer.data)
