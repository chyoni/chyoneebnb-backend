from django.db import models
from common.models import CommonModel


class Booking(CommonModel):

    """Booking Model Definition"""

    class BookingKindChoices(models.TextChoices):
        ROOM = ("room", "Room")
        EXPERIENCE = ("experience", "Experience")

    kind = models.CharField(max_length=15, choices=BookingKindChoices.choices)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="bookings"
    )
    room = models.ForeignKey(
        "rooms.Room",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="bookings",
    )
    check_in = models.DateField(null=True, blank=True, help_text="for reservation room")
    check_out = models.DateField(
        null=True, blank=True, help_text="for reservation room"
    )
    experience_time = models.DateTimeField(
        null=True, blank=True, help_text="for experience"
    )
    guests = models.PositiveIntegerField()

    def __str__(self) -> str:
        return f"{self.kind.title()} - {self.user}"
