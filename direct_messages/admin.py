from django.contrib import admin
from .models import ChatRoom, Message


@admin.register(ChatRoom)
class ChatRoomAdmin(admin.ModelAdmin):

    list_display = ("id", "__str__", "created_at")


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):

    list_display = ("id", "user", "text", "chat_room", "created_at")

    list_filter = ("user", "chat_room", "created_at")
