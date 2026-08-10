from django.core.mail import send_mail
from datetime import datetime
import smtplib

from .models import SendingLog, Sending, Recipient


def send_email(sending: Sending):
    subject = sending.message.theme
    message = sending.message.body

    recipient_list = list(sending.recipients.values_list('email', flat=True))
    from_email = 'usr123qwe@yandex.ru'


    sent_count = send_mail(subject, message, from_email, recipient_list)

    email_done = 'Не успешно'
    server_resp = 'Произошла ошибка при рассылке'

    if sent_count > 0:
        email_done = 'Успешно'
        server_resp = 'Рассылка выполнена успешно!'


    sending_log_record = SendingLog()
    sending_log_record.attempt_time = datetime.now()
    sending_log_record.sending = sending
    sending_log_record.status = email_done
    sending_log_record.server_response = server_resp
    sending_log_record.save()

def get_sending_count():
    return str(Sending.objects.all().count())

def active_sending_count():
    started_sendings = Sending.objects.filter(status='Запущена')
    active_sendings = []

    for sending in started_sendings:
        start_time = datetime(sending.start_time.year, sending.start_time.month, sending.start_time.day
                              , sending.start_time.hour, sending.start_time.minute, sending.start_time.second)
        end_time = datetime(sending.end_time.year, sending.end_time.month, sending.end_time.day
                              , sending.end_time.hour, sending.end_time.minute, sending.end_time.second)

        if start_time <= datetime.now() and end_time >= datetime.now():
            active_sendings.append(sending)

    active_count = len(active_sendings)

    return active_count

def get_recipients_count():
    return Recipient.objects.all().count()

