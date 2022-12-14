from django.contrib import admin
from .models import Room, Amenity


# Custom action on admin panel. refer to -> https://docs.djangoproject.com/en/4.1/ref/contrib/admin/actions/#writing-action-functions
@admin.action(description="Set all prices to zero")
def clear_prices(model_admin, request, queryset):
    for room in queryset.all():
        room.price = 0
        room.save()
    return


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):

    """Room admin"""

    # Declare my custom actions
    actions = (clear_prices,)

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
                "category",
            )
        },
    ), ("More About the Space", {"classes": ("wide"), "fields": ("amenities",)})

    list_display = (
        "id",
        "name",
        "country",
        "price",
        "city",
        "total_rating",
        "total_amenities",
        "kind",
        "owner",
    )
    filter_horizontal = ("amenities",)
    list_filter = ("city", "kind", "country", "pet_friendly", "amenities")
    search_fields = (
        "name",
        "price",
    )
    ordering = ("-created_at",)


@admin.register(Amenity)
class AmenityAdmin(admin.ModelAdmin):

    list_display = ("id", "name", "description", "created_at", "updated_at")
