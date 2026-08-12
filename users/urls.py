from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from users.apps import UsersConfig
from users.views import RegisterView, email_verification, UserListView, UserBlockView


app_name = UsersConfig.name

urlpatterns = [
    path('login/', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('messagesender:index')), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('<int:pk>/block-user/', UserBlockView.as_view(), name='user_block'),

]