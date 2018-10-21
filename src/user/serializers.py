from rest_framework import serializers

from . import models, views


class UserSerializer(serializers.Serializer):
    username = serializers.CharField()
    name = serializers.CharField()

    class Meta:
        fields = ("username", "name")
