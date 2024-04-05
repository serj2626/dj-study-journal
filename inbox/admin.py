from django.contrib import admin
from .models import Chat, Message


@admin.register(Chat)
class ChatAdmin(admin.ModelAdmin):
    '''Admin View for Chat'''

    list_display = ('sender', 'receiver', 'created', 'updated')


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    '''Admin View for Message)'''

    list_display = ('chat', 'sender', 'receiver',  'created', 'updated', )
