from django.urls import reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail

from .forms import UserRegisterForm

class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('messagesender:index')

    def form_valid(self, form):
        user = form.save()
        self.send_welcome_email(user.email)

        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        from_email = 'usr123qwe@yandex.ru'
        send_mail(subject, message, from_email, recipient_list)
