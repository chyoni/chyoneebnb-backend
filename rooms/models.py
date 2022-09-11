from django.db import models


class Room(models.Model):

    """Model Definition for Room"""

    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = ("entire_place", "Entire Place")
        PRIVATE_ROOM = ("private_room", "Private Room")
        SHARED_ROOM = ("shared_room", "Shared Room")

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50, default="Korea")
    city = models.CharField(max_length=80, default="Seoul")
    price = models.PositiveIntegerField()
    rooms_count = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=250)
    pet_friendly = models.BooleanField(default=True)
    kind = models.CharField(max_length=20, choices=RoomKindChoices.choices)
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="rooms"
    )


class Amenity(models.Model):

    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True, default="")
