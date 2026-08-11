from django.contrib import admin

from .models import Recipient, Sending, Message

@admin.register(Recipient)
class Recipient(admin.ModelAdmin):

    list_display = ('fullname', 'email', )
    search_fields = ('fullname', 'email', )

@admin.register(Sending)
class Sending(admin.ModelAdmin):

    list_display = ('start_time', 'end_time', 'message')
    search_fields = ('message', 'start_time', 'end_time')

@admin.register(Message)
class Message(admin.ModelAdmin):

    list_display = ('theme', 'body' )
    search_fields = ('theme', )