from django.db import models
from common.models import CommonModel


class Wishlist(CommonModel):

    """Wishlist Model Definition"""

    name = models.CharField(max_length=150)
    rooms = models.ManyToManyField("rooms.Room", blank=True)
    experiences = models.ManyToManyField("experiences.Experience", blank=True)
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="wishlists"
    )
