from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)
from django.db import models
from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True, unique=True)
    name = models.CharField(max_length=50, unique=True, blank=False, null=True, verbose_name="Имя")
    surname = models.CharField(max_length=50, unique=True, blank=False, null=True, verbose_name="Фамилия")
    age = models.IntegerField(max_length=120, unique=True, blank=False, null=True, verbose_name="Возраст")
    doctor = models.CharField(max_length=100, unique=True, blank=False, verbose_name="Врач")
    number = models.IntegerField(max_length=25, unique=True, blank=False, null=True, verbose_name="Номер")
    is_active = models.BooleanField(default=True, verbose_name="Активность")
    is_staff = models.BooleanField(default=False, verbose_name="Менеджер")
    is_superuser = models.BooleanField(default=False, verbose_name="Суперпользователь")

    USERNAME_FIELD = 'name'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    @property
    def get_username(self):
        return f'{self.name} {self.surname}'

    def __str__(self):
        return self.name