from django.core.validators import EmailValidator
from django.core.exceptions import ValidationError
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TaskUserSerializer
from .models import TaskUser
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework import status


@api_view(["GET"])
def get_users(request):
    users = TaskUser.objects.all()
    serializer = TaskUserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def register(request):

    email = request.data["email"]
    try:
        EmailValidator()(email)
    except ValidationError:
        return Response("Email should be valid!!!")

    user = TaskUser.objects.create_user(
        username=request.data["username"],
        email=email,
        password=request.data["password"],
    )
    user.is_active = True
    user.save()
    return Response("New user created")
