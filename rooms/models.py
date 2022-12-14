from django.db import models
from common.models import CommonModel


class Room(CommonModel):

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
    amenities = models.ManyToManyField("rooms.Amenity", blank=True)
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        related_name="rooms",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name

    def total_amenities(self) -> int:
        return self.amenities.all().count()

    def total_rating(self) -> float:
        all_reviews = self.reviews.all()
        total = 0
        if len(all_reviews) == 0:
            return 0
        for review in all_reviews:
            total += review.rating
        return round(total / len(all_reviews), 1)


class Amenity(CommonModel):

    """Amenity Definition"""

    name = models.CharField(max_length=150)
    description = models.CharField(max_length=150, blank=True, null=True, default="")

    def __str__(self) -> str:
        return self.name

    class Meta:
        verbose_name_plural = "Amenities"
