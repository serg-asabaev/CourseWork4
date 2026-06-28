from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from messagesender.models import Recipient


class IndexView(TemplateView):
    model = Recipient
    template_name = "messagesender/base.html"

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