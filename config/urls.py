from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from messagesender.apps import MessagesenderConfig

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("messagesender.urls", namespace='messagesender')),
]
