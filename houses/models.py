from django.db import models


class House(models.Model):

    """Model Definition for House"""

    name = models.CharField(max_length=140)
    price = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(max_length=200)
