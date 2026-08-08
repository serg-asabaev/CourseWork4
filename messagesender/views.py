from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from messagesender.models import Recipient, Message, Sending


class IndexView(TemplateView):
    model = Recipient
    template_name = "messagesender/base.html"

# Получатель
class RecipientListView(ListView):
    model = Recipient
    context_object_name = 'recipients'

class RecipientDetailView(DetailView):
    model = Recipient
    context_object_name = 'recipient'

class RecipientCreateView(CreateView):
    model = Recipient
    context_object_name = 'recipient'
    fields = ('fullname', 'email', 'comment')
    success_url = reverse_lazy('messagesender:recipient_list')

class RecipientUpdateView(UpdateView):
    model = Recipient
    context_object_name = 'recipient'
    fields = ('fullname', 'email', 'comment')
    success_url = reverse_lazy('messagesender:recipient_list')

class RecipientDeleteView(DeleteView):
    model = Recipient
    context_object_name = 'recipient'
    success_url = reverse_lazy('messagesender:recipient_list')

# Сообщение
class MessageListView(ListView):
    model = Message
    context_object_name = 'messages'

class MessageDetailView(DetailView):
    model = Message
    context_object_name = 'message'

class MessageCreateView(CreateView):
    model = Message
    context_object_name = 'message'
    fields = ('theme', 'body')
    success_url = reverse_lazy('messagesender:message_list')

class MessageUpdateView(UpdateView):
    model = Message
    context_object_name = 'message'
    fields = ('theme', 'body')
    success_url = reverse_lazy('messagesender:message_list')

class MessageDeleteView(DeleteView):
    model = Message
    context_object_name = 'message'
    success_url = reverse_lazy('messagesender:message_list')

# Рассылка

class SendingListView(ListView):
    model = Sending
    context_object_name = 'sendings'

class SendingDetailView(DetailView):
    model = Sending
    context_object_name = 'sending'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()  # ← пересчёт и сохранение статуса
        return obj

class SendingCreateView(CreateView):
    model = Sending
    context_object_name = 'sending'
    fields = ('start_time', 'end_time', 'message', 'recipients')
    success_url = reverse_lazy('messagesender:sending_list')

class SendingUpdateView(UpdateView):
    model = Sending
    context_object_name = 'sending'
    fields = ('start_time', 'end_time', 'message', 'recipients')
    success_url = reverse_lazy('messagesender:sending_list')

class SendingDeleteView(DeleteView):
    model = Sending
    context_object_name = 'sending'
    success_url = reverse_lazy('messagesender:sending_list')