from .models import User
from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import serializers


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    password2 = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = User
        fields = 'name, surname, age, doctor, number, password, password2'.split()

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
