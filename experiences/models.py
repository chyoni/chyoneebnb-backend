from django.db import models
from common.models import CommonModel


class Experience(CommonModel):

    """Experience Model Definition"""

    name = models.CharField(max_length=200)
    country = models.CharField(max_length=50, default="Korea")
    city = models.CharField(max_length=80, default="Seoul")
    price = models.PositiveIntegerField()
    host = models.ForeignKey(
        "users.User", related_name="experiences", on_delete=models.CASCADE
    )
    address = models.CharField(max_length=250)
    start = models.DateTimeField()
    end = models.DateTimeField()
    perks = models.ManyToManyField("experiences.Perk")
    category = models.ForeignKey(
        "categories.Category",
        on_delete=models.SET_NULL,
        related_name="experiences",
        null=True,
        blank=True,
    )

    def __str__(self) -> str:
        return self.name


class Perk(CommonModel):

    """What is included on an Experience"""

    name = models.CharField(max_length=150)
    detail = models.CharField(max_length=250, blank=True, null=True, default="")
    explanation = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.name
