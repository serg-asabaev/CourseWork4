from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseForbidden
from django.contrib.auth.mixins import LoginRequiredMixin

from messagesender.models import Recipient, Message, Sending, SendingLog
from messagesender.forms import SendingForm, SendingSendForm
from messagesender.services import send_email, get_sending_count, active_sending_count, get_recipients_count

class IndexView(TemplateView):
    template_name = "messagesender/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['sendings_count'] = get_sending_count()
        context['active_sendings'] = active_sending_count()
        context['recipients_count'] = get_recipients_count()
        return context

# Получатель
class RecipientListView(LoginRequiredMixin, ListView):
    model = Recipient
    context_object_name = 'recipients'
    login_url = reverse_lazy('users:login')

class RecipientDetailView(LoginRequiredMixin, DetailView):
    model = Recipient
    context_object_name = 'recipient'

class RecipientCreateView(LoginRequiredMixin, CreateView):
    model = Recipient
    context_object_name = 'recipient'
    fields = ('fullname', 'email', 'comment')
    success_url = reverse_lazy('messagesender:recipient_list')

class RecipientUpdateView(LoginRequiredMixin, UpdateView):
    model = Recipient
    context_object_name = 'recipient'
    fields = ('fullname', 'email', 'comment')
    success_url = reverse_lazy('messagesender:recipient_list')

class RecipientDeleteView(LoginRequiredMixin, DeleteView):
    model = Recipient
    context_object_name = 'recipient'
    success_url = reverse_lazy('messagesender:recipient_list')


# Сообщение
class MessageListView(LoginRequiredMixin, ListView):
    model = Message
    context_object_name = 'messages'
    login_url = reverse_lazy('users:login')

class MessageDetailView(LoginRequiredMixin, DetailView):
    model = Message
    context_object_name = 'message'

class MessageCreateView(LoginRequiredMixin, CreateView):
    model = Message
    context_object_name = 'message'
    fields = ('theme', 'body')
    success_url = reverse_lazy('messagesender:message_list')

class MessageUpdateView(LoginRequiredMixin, UpdateView):
    model = Message
    context_object_name = 'message'
    fields = ('theme', 'body')
    success_url = reverse_lazy('messagesender:message_list')

class MessageDeleteView(LoginRequiredMixin, DeleteView):
    model = Message
    context_object_name = 'message'
    success_url = reverse_lazy('messagesender:message_list')


# Рассылка
class SendingListView(LoginRequiredMixin, ListView):
    model = Sending
    context_object_name = 'sendings'
    login_url = reverse_lazy('users:login')

class SendingDetailView(LoginRequiredMixin, DetailView):
    model = Sending
    context_object_name = 'sending'

    def get_object(self, queryset=None):
        obj = super().get_object(queryset)
        obj.update_status()  # ← пересчёт и сохранение статуса
        return obj

class SendingCreateView(LoginRequiredMixin, CreateView):
    model = Sending
    context_object_name = 'sending'
    form_class = SendingForm
    success_url = reverse_lazy('messagesender:sending_list')

class SendingUpdateView(LoginRequiredMixin, UpdateView):
    model = Sending
    context_object_name = 'sending'
    form_class = SendingForm
    success_url = reverse_lazy('messagesender:sending_list')

class SendingDeleteView(LoginRequiredMixin, DeleteView):
    model = Sending
    context_object_name = 'sending'
    success_url = reverse_lazy('messagesender:sending_list')

class SendingSendView(LoginRequiredMixin, View):
    model = Sending
    context_object_name = 'sending'
    success_url = reverse_lazy('messagesender:sending_list')

    def post(self, request, pk):
        sending = get_object_or_404(Sending, id=pk)

        send_email(sending)

        return redirect('messagesender:sending_list')

