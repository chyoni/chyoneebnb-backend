from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import NotFound
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Wishlist
from rooms.models import Room
from .serializers import WishlistSerializer


class Wishlists(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        all_wishlists = Wishlist.objects.filter(user=request.user)
        serializer = WishlistSerializer(instance=all_wishlists, many=True, context={"request": request})
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            wishlist = serializer.save(user=request.user)
            return Response(status=status.HTTP_201_CREATED, data=WishlistSerializer(instance=wishlist).data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)
        

class WishlistDetail(APIView):

    def get_object(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        wishlist = self.get_object(pk=pk, user=request.user)
        serializer = WishlistSerializer(instance=wishlist)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, pk):
        wishlist = self.get_object(pk=pk, user=request.user)
        serializer = WishlistSerializer(instance=wishlist, data=request.data, partial=True)
        if serializer.is_valid():
            wishlist = serializer.save()
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.errors)

    def delete(self, request, pk):
        wishlist = self.get_object(pk=pk, user=request.user)
        wishlist.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class WishlistRoomToggle(APIView):

    def get_list(self, pk, user):
        try:
            return Wishlist.objects.get(pk=pk, user=user)
        except Wishlist.DoesNotExist:
            raise NotFound
        
    def get_room(self, pk):
        try:
            return Room.objects.get(pk=pk)
        except Room.DoesNotExist:
            raise NotFound

    def put(self, request, pk, room_pk):
        wishlist = self.get_list(pk, request.user)
        room = self.get_room(room_pk)
        if wishlist.rooms.filter(pk=room.pk).exists():
            wishlist.rooms.remove(room)
        else:
            wishlist.rooms.add(room)
        return Response(status=status.HTTP_200_OK, data=WishlistSerializer(instance=wishlist).data)