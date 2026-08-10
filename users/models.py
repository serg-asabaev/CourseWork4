from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):

    username = None

    email = models.EmailField(unique=True, verbose_name='Email')
    phone = models.CharField(max_length=35, blank=True, null=True, verbose_name="Телефон", help_text="Введите номер телефона")
    country = models.CharField(max_length=50, blank=True, null=True, verbose_name="Страна", help_text="Введите страну")

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.email
