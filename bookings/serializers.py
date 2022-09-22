from django.utils import timezone
from rest_framework.serializers import ModelSerializer, DateField, ValidationError
from .models import Booking


class CreateRoomBookingSerializer(ModelSerializer):

    check_in = DateField()
    check_out = DateField()

    class Meta:
        model = Booking
        fields = ("check_in", "check_out", "guests")

    def validate_check_in(self, data):
        now = timezone.localtime(timezone.now()).date()
        if now > data:
            raise ValidationError("Can't book in the past!")
        return data

    def validate_check_out(self, data):
        now = timezone.localtime(timezone.now()).date()
        if now > data:
            raise ValidationError("Can't book in the past!")
        return data

    def validate(self, attrs):
        if attrs["check_out"] <= attrs["check_in"]:
            raise ValidationError("Check in should be smaller than check out")
        if Booking.objects.filter(
            check_in__lte=attrs["check_out"],
            check_out__gte=attrs["check_in"]
        ).exists():
            raise ValidationError("This day already taken")
        return attrs 


class PublicBookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"