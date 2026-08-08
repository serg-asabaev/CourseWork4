from datetime import datetime
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

class Message(models.Model):
    theme = models.CharField(max_length=150, verbose_name="Тема")
    body = models.TextField(verbose_name="Тело письма")

    def __str__(self):
        return f'{self.theme}: {self.body[:100]}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
        ordering = ['theme', ]

class Sending(models.Model):
    start_time = models.DateTimeField(verbose_name='Дата и время начала отправки')
    end_time = models.DateTimeField(verbose_name='Дата и время окончания отправки')

    status = models.CharField(max_length=50, verbose_name='Статус')

    message = models.ForeignKey(Message, on_delete=models.CASCADE, related_name='message', verbose_name='Сообщение')
    recipients = models.ManyToManyField(Recipient, related_name='recipient', verbose_name='Получатели сообщения')

    def update_status(self):
        now_time = datetime.now()

        start_time = datetime(self.start_time.year, self.start_time.month, self.start_time.day,
                              self.start_time.hour, self.start_time.minute, self.start_time.second)
        end_time = datetime(self.end_time.year, self.end_time.month, self.end_time.day,
                              self.end_time.hour, self.end_time.minute, self.end_time.second)

        if start_time > now_time:
            self.status = 'Создана'
        elif start_time <= now_time <= end_time:
            self.status = 'Запущена'
        else:
            self.status = 'Завершена'
        self.save()