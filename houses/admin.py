from atexit import register
from django.contrib import admin
from . import models


@admin.register(models.House)
class HouseAdmin(admin.ModelAdmin):

    list_display = [
        "id",
        "name",
        "price_per_night",
        "description",
        "address",
        "pets_allowed",
    ]
    list_filter = ["pets_allowed", "price_per_night"]
    search_fields = ["address", "name"]
