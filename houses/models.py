from django.db import models


class House(models.Model):

    """Model Definition for House"""

    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField(help_text="Positive Numbers Only")
    description = models.TextField()
    address = models.CharField(max_length=200)
    pets_allowed = models.BooleanField(
        default=True, help_text="Does this house pets allowed?"
    )
    owner = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="houses"
    )
