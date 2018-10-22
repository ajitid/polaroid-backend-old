from rest_framework import serializers

from . import models, views


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.User
        fields = ("username", "name")
