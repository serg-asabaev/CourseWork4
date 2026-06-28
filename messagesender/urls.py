from django.urls import path
from . import views

app_name = 'messagesender'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('recipients/list', views.RecipientListView.as_view(), name='recipient_list'),
    path('recipients/<int:pk>/detail/', views.RecipientDetailView.as_view(), name='recipient_detail'),
    path('recipients/create', views.RecipientCreateView.as_view(), name='recipient_create'),
    path('recipients/<int:pk>/update/', views.RecipientUpdateView.as_view(), name='recipient_update'),
    path('recipients/<int:pk>/delete/', views.RecipientDeleteView.as_view(), name='recipient_delete'),
]