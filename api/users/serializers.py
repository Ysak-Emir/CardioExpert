from rest_framework.validators import UniqueValidator

from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework import serializers
from django.utils.crypto import get_random_string
from django.core.mail import send_mail

User = get_user_model()


class UserRegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = 'id email name surname age doctor number password password2'.split()

    def save(self, *args, **kwargs):
        user = User(
            name=self.validated_data["name"],
            surname=self.validated_data["surname"],
            age=self.validated_data["age"],
            doctor=self.validated_data["doctor"],
            number=self.validated_data["number"],
        )
        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({password: "Пароли не совпадают!"})
        user.set_password(password)
        user.save()
        return user


class LoginUserSerializer(serializers.Serializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    def validate(self, attrs):
        username = attrs.get('username')
        password = attrs.get('password')

        if username and password:
            user = authenticate(request=self.context.get('request'),
                                username=username, password=password)
            if not user:
                msg = 'Доступ запрещен: неправильное имя пользователя или пароль.'
                raise serializers.ValidationError({"password": msg}, code='authorization')
        else:
            msg = 'Требуются как «имя пользователя», так и «пароль».'
            raise serializers.ValidationError(msg, code='authorization')
        attrs['user'] = user
        return
