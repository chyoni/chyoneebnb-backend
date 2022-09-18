from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import NotFound
from .models import Amenity
from .serializers import AmenitySerializer


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
