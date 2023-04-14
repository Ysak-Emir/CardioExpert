from django.contrib.auth.models import (
    BaseUserManager,
)


class CustomUserManager(BaseUserManager):
    def _create_user(self, name, surname, age, doctor, number, password, is_staff, is_superuser, **extra_fields):
        if not name:
            raise ValueError("Вы не ввели ваше имя!")
        if not surname:
            raise ValueError("Вы не ввели вашу фамилию")
        if not age:
            raise ValueError("Вы не ввели ваш возраст!")
        if not doctor:
            raise ValueError("Вы не ввели ФИО вашего врача!")
        if not number:
            raise ValueError("Вы не ввели ваш номер!")
        if not password:
            raise ValueError("Вы не ввели пароль!")
        user = self.model(
            name=name,
            surname=surname,
            age=age,
            doctor=doctor,
            number=number,
            password=password,
            is_active=True,
            is_staff=is_staff,
            is_superuser=is_superuser,
            **extra_fields
        )
        if password:
            user.set_password(password)
        user.save(using=self._db)
        return user

    def _create_superuser(self, name, password, **extra_fields):
        if not name:
            raise ValueError("Вы не ввели ваше имя !")
        if not password:
            raise ValueError("Вы не ввели пароль!")
        superuser = self.model(
            name=name,
            password=password,
            is_active=True,
            is_staff=True,
            is_superuser=True,
            **extra_fields
        )
        if password:
            superuser.set_password(password)
        superuser.save(using=self._db)
        return superuser

    def create_user(
            self,
            name,
            surname,
            age,
            doctor,
            number,
            password=None,
            **extra_fields
    ):

        return self._create_user(name, surname, age, doctor, number, password, is_staff=False, is_superuser=False,
                                 **extra_fields)

    def create_superuser(
            self,
            name,
            password=None,
    ):

        superuser = self._create_superuser(name, password)
        superuser.save(using=self._db)
        return superuser
