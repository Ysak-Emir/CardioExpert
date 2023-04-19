import rest_framework_simplejwt
from django.contrib.auth import authenticate
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.shortcuts import get_object_or_404
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from rest_framework import generics, permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken

from api.users import serializers
from api.users.models import User
from api.users.serializers import UserRegisterSerializer, LogoutSerializer, EmailSerializer
from config import settings


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


class LogoutAPIView(generics.GenericAPIView):
    serializer_class = LogoutSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"message": "Вы вышли из системы!"}, status=status.HTTP_204_NO_CONTENT)


PASSWORD_RESET_URL = 'reset-password'
JWT_SECRET_KEY = settings.SECRET_KEY


class PasswordReset(generics.GenericAPIView):
    """
    Запрос на сброс пароля
    """
    serializer_class = EmailSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        """
        Создание токена
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        email = serializer.validated_data['email']
        user = get_object_or_404(User, email=email)

        encoded_pk = urlsafe_base64_encode(force_bytes(user.pk))
        token = PasswordResetTokenGenerator().make_token(user)
        reset_url = reverse(PASSWORD_RESET_URL, kwargs={'encoded_pk': encoded_pk, 'token': token})
        reset_link = f'http://localhost:8000{reset_url}'

        # отправить reset_link по почте пользователю.

        message = f'Ваша ссылка для сброса пароля: {reset_link}'
        return Response({'message': message}, status=status.HTTP_200_OK)


class ResetPasswordAPI(generics.GenericAPIView):
    """
    Проверка и сброс пароля Токена
    """

    serializer_class = serializers.ResetPasswordSerializer
    permission_classes = (IsAuthenticated,)

    def patch(self, request, *args, **kwargs):
        """
        Проверка токена и encoded_pk, а затем сброс пароля
        """
        serializer = self.serializer_class(
            data=request.data, context={"kwargs": kwargs}
        )
        serializer.is_valid(raise_exception=True)
        return Response(
            {"message": "Восстановление пароля завершено"},
            status=status.HTTP_200_OK,
        )
