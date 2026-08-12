from django.contrib import admin

from users.models import User


@admin.register(User)
class Sending(admin.ModelAdmin):

    list_display = ('id', 'email',)
