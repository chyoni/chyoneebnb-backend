from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import Amenity, Room
from users.serializers import TinyUserSerializer
from categories.serializers import CategorySerializer
from medias.serializers import PhotoSerializer
from wishlists.models import Wishlist

class AmenitySerializer(ModelSerializer):
    class Meta:
        model = Amenity
        fields = ("pk", "name", "description")


class RoomDetailSerializer(ModelSerializer):

    owner = TinyUserSerializer(read_only=True)
    amenities = AmenitySerializer(read_only=True, many=True)
    category = CategorySerializer(read_only=True)
    rating = SerializerMethodField()
    is_liked = SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = "__all__"

    def get_rating(self, room):
        return room.total_rating()

    def get_is_liked(self, room):
        request = self.context['request']
        return Wishlist.objects.filter(user=request.user, rooms__pk=room.pk).exists()


class RoomListSerializer(ModelSerializer):

    rating = SerializerMethodField()
    is_liked = SerializerMethodField()
    photos = PhotoSerializer(many=True, read_only=True)

    class Meta:
        model = Room
        fields = ["pk", "name", "country", "city", "price", "rating", "photos"]

    def get_rating(self, room):
        return room.total_rating()

    def get_is_liked(self, room):
        request = self.context['request']
        return Wishlist.objects.filter(user=request.user, rooms__pk=room.pk).exists()
