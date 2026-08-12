from django.core.mail import send_mail
from django.core.cache import cache
from datetime import datetime

from .models import SendingLog, Sending, Message, Recipient
from config.settings import CACHE_ENABLED

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

def get_success_attempts_count(sending: Sending):

    attempts = SendingLog.objects.filter(sending=sending)
    success_attempts = []

    for attempt in attempts:
        if attempt.status == 'Успешно':
            success_attempts.append(attempt)

    return len(success_attempts)

def get_failed_attempts_count(sending: Sending):

    attempts = SendingLog.objects.filter(sending=sending)
    failed_attempts = []

    for attempt in attempts:
        if attempt.status == 'Не успешно':
            failed_attempts.append(attempt)

    return len(failed_attempts)

def get_total_emails(sending: Sending):
    return SendingLog.objects.filter(sending=sending).count()

def stop_sending(sending: Sending):

    sending.status = 'Завершена'
    now_date = datetime.now()
    end_time = datetime(now_date.year, now_date.month, now_date.day, 0, 0, 0)
    sending.end_time = end_time

    sending.save()

def get_recipient_from_cache():
    """Получает данные о клиенте из кэша, если кэш пуст то возвращает данные из базы"""
    if not CACHE_ENABLED:
        return Recipient.objects.all()

    key = "recipients_list"
    recipients = cache.get(key)
    if recipients is not None:
        return recipients

    recipients = Recipient.objects.all()
    cache.set(key, recipients, 60)

    return recipients

def get_message_from_cache():
    """Получает данные о сообщении из кэша, если кэш пуст то возвращает данные из базы"""
    if not CACHE_ENABLED:
        return Message.objects.all()

    key = "messages_list"
    messages = cache.get(key)
    if messages is not None:
        return messages

    messages = Message.objects.all()
    cache.set(key, messages, 60)

    return messages

def get_sending_from_cache():
    """Получает данные о рассылке из кэша, если кэш пуст то возвращает данные из базы"""
    if not CACHE_ENABLED:
        return Sending.objects.all()

    key = "products_list"
    sendings = cache.get(key)
    if sendings is not None:
        return sendings

    sendings = Sending.objects.all()
    cache.set(key, sendings, 60)

    return sendings