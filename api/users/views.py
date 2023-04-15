import rest_framework_simplejwt
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


class RegisterUserAPIView(CreateAPIView):
    """
    Регистрация пользователя
    """
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
            return Response({"message": "Что-то пошло не так!",
                             "data": data})


class UserLoginAPIView(generics.GenericAPIView):
    """
    Авторизация пользователя
    """
    permission_classes = (permissions.AllowAny,)
    serializer_class = serializers.LoginUserSerializer

    def post(self, request, format=None):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(email=serializer.validated_data['email'],
                            password=serializer.validated_data['password'])
        if user:
            refresh = rest_framework_simplejwt.tokens.RefreshToken.for_user(user)
            return Response({"refresh": str(refresh), "access": str(refresh.access_token)},
                            status=status.HTTP_202_ACCEPTED)

    def get_serializer(self, *args, **kwargs):
        kwargs['context'] = self.get_serializer_context()
        return self.serializer_class(*args, **kwargs)
