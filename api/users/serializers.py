from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.http import urlsafe_base64_decode
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.tokens import RefreshToken
from django.core.mail import send_mail
from django.conf import settings
from .models import User
from rest_framework import serializers, generics, status
from django.contrib.auth import authenticate
from rest_framework import serializers
from django.contrib.auth.forms import PasswordResetForm
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from rest_framework.response import Response
from django.core.mail import send_mail


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, write_only=True)
    name = serializers.CharField(max_length=50, min_length=3, write_only=True)
    surname = serializers.CharField(max_length=50, min_length=3, write_only=True)
    age = serializers.IntegerField(max_value=120, min_value=3, write_only=True)
    number = serializers.IntegerField(min_value=3, write_only=True)
    doctor = serializers.CharField(min_length=3, max_length=80, write_only=True)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = '__all__'

    def validate_email(self, email):
        if User.objects.filter(email=email).exists():
            raise serializers.ValidationError('Данная электронная почта уже используется!')
        return email

    def create(self, validated_data):
        password = validated_data.pop('password')
        password2 = validated_data.pop('password2')
        if password != password2:
            raise serializers.ValidationError({'password': 'Пароли не совпадают!'})
        user = User.objects.create(**validated_data, is_email_verified=False)
        user.set_password(password)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField(label="email", write_only=True)
    password = serializers.CharField(label="password", style={'input_type': 'password'}, trim_whitespace=False,
                                     write_only=True)


    def validate(self, attrs):
        email = attrs.get('email')
        password = attrs.get('password')

        if not email or not password:
            msg = 'Требуются как «email», так и «пароль».'
            raise serializers.ValidationError(msg, code='authorization')

        user = authenticate(request=self.context.get('request'),
                            username=email, password=password)

        if not user:
            msg = 'Доступ запрещен: неправильное email или пароль.'
            raise serializers.ValidationError({"password": msg}, code='authorization')

        attrs['user'] = user
        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField()

    def validate(self, attrs):
        self.token = attrs['refresh']

        return attrs

    def save(self, **kwargs):
        try:
            RefreshToken(self.token).blacklist()
        except TokenError:
            self.fail('bad token')


class PasswordResetSerializer(serializers.Serializer):
    email = serializers.EmailField()


class PasswordResetConfirmSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=128)


