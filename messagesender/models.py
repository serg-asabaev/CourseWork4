from django.db import models

class Recipient(models.Model):
    email = models.CharField(max_length=100, unique=True, verbose_name="Email")
    fullname = models.CharField(max_length=150, verbose_name="Ф.И.О.")
    comment = models.TextField(verbose_name="Комментарий")

    def __str__(self):
        return f'{self.fullname} {self.email}'

    class Meta:
        verbose_name = 'Получатель сообщения'
        verbose_name_plural = 'Получатели сообщения'
        ordering = ['fullname',]
