from django.urls import path
from . import views

app_name = 'messagesender'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recipients/list/', views.RecipientListView.as_view(), name='recipient_list'),
    path('recipients/<int:pk>/detail/', views.RecipientDetailView.as_view(), name='recipient_detail'),
    path('recipients/create/', views.RecipientCreateView.as_view(), name='recipient_create'),
    path('recipients/<int:pk>/update/', views.RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipients/<int:pk>/delete/', views.RecipientDeleteView.as_view(), name='recipient_delete'),
    path('messages/list/', views.MessageListView.as_view(), name='message_list'),
    path('messages/<int:pk>/detail/', views.MessageDetailView.as_view(), name='message_detail'),
    path('message/create/', views.MessageCreateView.as_view(), name='message_create'),
    path('messages/<int:pk>/update', views.MessageUpdateView.as_view(), name='message_update'),
    path('messages/<int:pk>/delete', views.MessageDeleteView.as_view(), name='message_delete'),
    path('sendings/list/', views.SendingListView.as_view(), name='sending_list'),
    path('sendings/<int:pk>/detail/', views.SendingDetailView.as_view(), name='sending_detail'),
    path('sendings/create/', views.SendingCreateView.as_view(), name='sending_create'),
    path('sendings/<int:pk>/update/', views.SendingUpdateView.as_view(), name='sending_update'),
    path('sendings/<int:pk>/delete/', views.SendingDeleteView.as_view(), name='sending_delete'),
    path('sendings/<int:pk>/send/', views.SendingSendView.as_view(), name='sending_send'),
]