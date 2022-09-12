from django.core.exceptions import ValidationError
from django.db import models
from common.models import CommonModel


class Review(CommonModel):

    """Review from a User to a Room or Experience"""

    def validate_rating(value):
        if value > 5:
            raise ValidationError(f"Rating is must belong to 0 - 5, but {value}")

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="reviews"
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="reviews",
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reviews",
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField(validators=[validate_rating])

    def __str__(self) -> str:
        return f"{self.user} / {self.rating}"
