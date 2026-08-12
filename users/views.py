import secrets

from django.urls import reverse_lazy, reverse
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic.edit import CreateView
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.views.generic import ListView, View

from .forms import UserRegisterForm
from config.settings import EMAIL_HOST_USER
from users.models import User


class RegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('messagesender:index')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False

        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'https://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейдите по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[
                user.email
            ]
        )
        self.send_welcome_email(user.email)
        return super().form_valid(form)

    def send_welcome_email(self, user_email):
        subject = 'Добро пожаловать в наш сервис'
        message = 'Спасибо, что зарегистрировались в нашем сервисе!'
        recipient_list = [user_email]
        from_email = 'usr123qwe@yandex.ru'
        send_mail(subject, message, from_email, recipient_list)

def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse('users:login'))

class UserListView(ListView):
    model = User
    context_object_name = 'users'
    login_url = reverse_lazy('users:login')


class UserBlockView(View):
    model = User
    context_object_name = 'user'
    success_url = reverse_lazy('users:user_list')

    def post(self, request, pk):
        user = get_object_or_404(User, id=pk)

        if user.is_active:
            user.is_active = False
        user.save()

        return redirect('users:user_list')
