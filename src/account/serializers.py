from rest_framework.serializers import HyperlinkedModelSerializer, HyperlinkedRelatedField

from . import models


class UserSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = models.User
        fields = ("name", "email")

