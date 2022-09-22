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


class PublicBookingSerializer(ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"