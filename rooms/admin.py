from django.contrib import admin
from .models import Room, Amenity


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        "Basic info",
        {
            "fields": (
                "name",
                "country",
                "price",
                "city",
                "kind",
                "owner",
                "toilets",
                "description",
                "address",
                "pet_friendly",
            )
        },
    ), ("More About the Space", {"classes": ("wide"), "fields": ("amenities",)})

    list_display = (
        "id",
        "name",
        "country",
        "price",
        "city",
        "kind",
        "owner",
    )
    filter_horizontal = ("amenities",)
    list_filter = ("city", "kind", "country", "pet_friendly", "amenities")
    ordering = ("-created_at",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = ("name", "description", "created_at", "updated_at")
