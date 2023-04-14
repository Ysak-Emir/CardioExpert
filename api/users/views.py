from django.contrib.auth import authenticate
from rest_framework import generics, permissions, status
from rest_framework.authentication import BasicAuthentication, SessionAuthentication
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from api.users import serializers
from api.users.models import User
from api.users.serializers import UserRegisterSerializer


class RegisterUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        data = request.data
        serializer = UserRegisterSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Регистрация прошла успешно!",
                "data": serializer.data
            }
            return Response(data=response)
        else:
            data = serializer.errors
            return Response({"message": "Что-то пошло не так! :(",
                             "data": data})
