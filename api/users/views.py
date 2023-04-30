import rest_framework_simplejwt
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from rest_framework import generics, permissions, status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.urls import reverse
from rest_framework_simplejwt.tokens import RefreshToken
from api.users import serializers
from api.users.models import User
from api.users.serializers import UserRegisterSerializer, LogoutSerializer, PasswordResetSerializer, \
    PasswordResetConfirmSerializer
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER


class RegisterUserAPIView(CreateAPIView):
    """
    Регистрация пользователя
    """
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializer
    permission_classes = (AllowAny,)

    def post(self, request, *args, **kwargs):
        try:
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
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




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


class PasswordResetView(generics.CreateAPIView):
    """
    Сброс пароля
    """
    serializer_class = PasswordResetSerializer
    permission_classes = (permissions.AllowAny, )

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        email = serializer.validated_data['email']
        user = User.objects.filter(email=email).first()

        if user:
            token = default_token_generator.make_token(user)
            self.send_reset_email(user, token)

        return Response({'message': 'Письмо для сброса пароля было успешно отправлено.'}, status=status.HTTP_200_OK)

    def send_reset_email(self, user, token):
        reset_url = self.get_reset_url(user, token)

        email_subject = 'Сброс пароля'
        email_message = f'Для сброса пароля перейдите по ссылке: {reset_url}'
        send_mail(email_subject, email_message, EMAIL_HOST_USER, [user.email])

    def get_reset_url(self, user, token):
        # Генерируйте URL для сброса пароля
        return self.request.build_absolute_uri(reverse('password-reset-confirm', args=[user.id, token]))


class PasswordResetConfirmView(generics.GenericAPIView):
    """
    Подтверждение сброса пароля
    """
    serializer_class = PasswordResetConfirmSerializer
    authentication_classes = []
    permission_classes = (permissions.AllowAny, )

    def post(self, request, user_id, token):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        user = User.objects.filter(id=user_id).first()

        if user and default_token_generator.check_token(user, token):
            new_password = serializer.validated_data['new_password']
            user.password = make_password(new_password)
            user.save()
            return Response({"message": "Пароль сброшен"},status=status.HTTP_200_OK)

        else:
            return Response({"message": "Что-то пошло не так! Возможно вы уже сбросили пароль."},status=status.HTTP_400_BAD_REQUEST)



