from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from . import models as category_models
from .serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):

    serializer_class = CategorySerializer
    queryset = category_models.Category.objects.all()
