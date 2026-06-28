from django.contrib import admin

from .models import Recipient

@admin.register(Recipient)
class Recipient(admin.ModelAdmin):

    list_display = ('fullname', 'email', )
    search_fields = ('fullname', 'email', )
