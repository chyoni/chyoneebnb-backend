from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from . import models as category_models
from .serializers import CategorySerializer


class Categories(APIView):
    def get(self, request):
        try:
            all_categories = category_models.Category.objects.all()
            serializer = CategorySerializer(instance=all_categories, many=True)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        except category_models.Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def post(self, request):
        serializer = CategorySerializer(data=request.data)
        if serializer.is_valid():
            new_category = serializer.save()
            return Response(
                CategorySerializer(instance=new_category).data,
                status=status.HTTP_201_CREATED,
            )
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST, data=serializer.data)


class Category(APIView):
    def get_object(self, pk):
        try:
            category = category_models.Category.objects.get(pk=pk)
            return category
        except category_models.Category.DoesNotExist:
            return None

    def get(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = CategorySerializer(instance=category)
            return Response(status=status.HTTP_200_OK, data=serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            serializer = CategorySerializer(
                instance=category, data=request.data, partial=True
            )
            if serializer.is_valid():
                updated_category = serializer.save()
                return Response(
                    status=status.HTTP_200_OK,
                    data=CategorySerializer(instance=updated_category).data,
                )
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        category = self.get_object(pk)
        if category is not None:
            category.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
