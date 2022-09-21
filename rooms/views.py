from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound, NotAuthenticated
from .models import Amenity, Room
from categories.models import Category
from .serializers import AmenitySerializer, RoomListSerializer, RoomDetailSerializer


class Amenities(APIView):
    def get(self, request):
        all_amenities = Amenity.objects.all()
        serializer = AmenitySerializer(instance=all_amenities, many=True)
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = AmenitySerializer(data=request.data)
        if serializer.is_valid():
            amenity = serializer.save()
            return Response(
                data=AmenitySerializer(instance=amenity).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)


class AmenityDetail(APIView):
    def get_object(self, pk):
        try:
            return Amenity.objects.get(pk=pk)
        except Amenity.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        return Response(
            AmenitySerializer(instance=self.get_object(pk)).data,
            status=status.HTTP_200_OK,
        )

    def put(self, request, pk):
        amenity = self.get_object(pk)
        serializer = AmenitySerializer(
            instance=amenity, data=request.data, partial=True
        )
        if serializer.is_valid():
            updated = serializer.save()
            return Response(
                data=AmenitySerializer(instance=updated).data, status=status.HTTP_200_OK
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk):
        amenity = self.get_object(pk)
        amenity.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class Rooms(APIView):
    def get(self, request):
        all_rooms = Room.objects.all()
        serializer = RoomListSerializer(instance=all_rooms, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        if request.user.is_authenticated:
            serializer = RoomDetailSerializer(data=request.data)
            if serializer.is_valid():
                category_pk = request.data.get("category")
                if category_pk is None:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={"error": "Category field is required"},
                    )
                try:
                    category = Category.objects.get(pk=category_pk)
                    if category.kind == Category.CategoryKindChoices.EXPERIENCES:
                        return Response(
                            status=status.HTTP_400_BAD_REQUEST,
                            data={
                                "error": "This category is only valid for experiences kind"
                            },
                        )
                except Category.DoesNotExist:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={"error": "category you given does not exist"},
                    )
                new_room = serializer.save(owner=request.user, category=category)
                amenities = request.data.get("amenities")
                if not amenities:
                    return Response(
                        status=status.HTTP_400_BAD_REQUEST,
                        data={"error": "Amenities data is empty"},
                    )
                for amenity in amenities:
                    try:
                        ame = Amenity.objects.get(pk=amenity)
                        new_room.amenities.add(ame)
                    except Amenity.DoesNotExist:
                        new_room.delete()
                        return Response(
                            status=status.HTTP_400_BAD_REQUEST,
                            data={
                                "error": f"That amenity with id: {amenity} does not found"
                            },
                        )
                serializer = RoomDetailSerializer(new_room)
                return Response(status=status.HTTP_201_CREATED, data=serializer.data)
            else:
                return Response(
                    status=status.HTTP_400_BAD_REQUEST, data=serializer.errors
                )
        else:
            raise NotAuthenticated


class RoomDetail(APIView):
    def get_object(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        room = self.get_object(pk)
        serializer = RoomDetailSerializer(instance=room)
        return Response(status=status.HTTP_200_OK, data=serializer.data)


# {
# "name": "Beautiful room for you",
# "price": 3000,
# "rooms_count": 3,
# "toilets": 3,
# "description": "Awesome Fucking Good",
# "address": "Chyonee house",
# "category": 1,
# "kind": "entire_place"
# }
