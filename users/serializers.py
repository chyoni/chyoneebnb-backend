from .models import User
from rest_framework.serializers import ModelSerializer


class TinyUserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["pk", "username", "nickname", "avatar"]
