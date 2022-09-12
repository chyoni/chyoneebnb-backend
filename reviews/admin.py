from django.contrib import admin
from .models import Review


class MoreThenThreeReviewsFilter(admin.SimpleListFilter):

    title: str = "By rating"

    parameter_name: str = "rated"

    def lookups(self, request, model_admin):
        return (("gt_3", "Greater then 3"), ("lt_3", "Less then 3"))

    def queryset(self, request, queryset):
        criteria = self.value()

        if criteria is None:
            return queryset
        if criteria == "gt_3":
            return queryset.filter(rating__gt=3)
        if criteria == "lt_3":
            return queryset.filter(rating__lt=3)


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):

    list_display = ("id", "__str__", "payload", "room", "experience")

    list_filter = (
        MoreThenThreeReviewsFilter,
        "rating",
        "room",
        "experience",
        "user__is_host",
    )
