from django.contrib import admin

from users.models import User


@admin.register(User)
class Product(admin.ModelAdmin):

    list_display = ('id', 'email',)
