from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    CLIENT = 'Клиент'
    SERVICECOMPANY = 'Сервисная организация'
    MANAGER = 'Менеджер'
    ADMIN = 'Администратор'

    CHOICES = [
        (CLIENT, 'Клиент'),
        (SERVICECOMPANY, 'Сервисная организация'),
        (MANAGER, 'Менеджер'),
        (ADMIN, 'Администратор'),
    ]

    role = models.CharField('Роль', max_length=30, choices=CHOICES)


    def __str__(self):
        return f'{self.first_name}'
    