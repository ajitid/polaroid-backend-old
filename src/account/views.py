from rest_framework import views, viewsets

from . import models, serializers


class UserView(viewsets.ModelViewSet):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer

