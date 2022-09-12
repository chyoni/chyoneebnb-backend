from django.db import models
from common.models import CommonModel


class ChatRoom(CommonModel):

    """Room Model Definition"""

    participants = models.ManyToManyField("users.User", related_name="chatrooms")

    def __str__(self) -> str:
        return "Chat room"


class Message(CommonModel):

    """Message Model Definition"""

    text = models.TextField()
    user = models.ForeignKey(
        "users.User",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="messages",
    )
    chat_room = models.ForeignKey(
        ChatRoom, on_delete=models.CASCADE, related_name="messages"
    )

    def __str__(self) -> str:
        return f"{self.user}: {self.text}"
