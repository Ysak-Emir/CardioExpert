from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.crypto import get_random_string
from django.core.mail import send_mail


# User = get_user_model()


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
        user = User.objects.create(**validated_data)
        user.set_password(password)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    email = serializers.CharField(label="email", write_only=True)
    password = serializers.CharField(label="password", style={'input_type': 'password'}, trim_whitespace=False,
                                     write_only=True)

    # class Meta:
    #     model = User
    #     fields = "email password".split()

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
