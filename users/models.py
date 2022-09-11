from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    """Model Definition for User"""

    class GenderChoices(models.TextChoices):
        # (DB displayed, Admin Panel displayed)
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    class CurrencyChoices(models.TextChoices):
        WON = ("won", "Korean Won")
        USD = ("usd", "Dollar")

    is_host = models.BooleanField(default=False, blank=True)
    nickname = models.CharField(max_length=80, blank=True)
    location = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    job = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=80, blank=True)
    avatar = models.ImageField(blank=True)
    gender = models.CharField(max_length=10, choices=GenderChoices.choices)
    language = models.CharField(max_length=2, choices=LanguageChoices.choices)
    currency = models.CharField(max_length=5, choices=CurrencyChoices.choices)
