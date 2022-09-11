from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):

    is_host = models.BooleanField(default=False, blank=True)
    location = models.CharField(max_length=200, blank=True)
    bio = models.CharField(max_length=200, blank=True)
    job = models.CharField(max_length=120, blank=True)
    phone = models.CharField(max_length=80, blank=True)
