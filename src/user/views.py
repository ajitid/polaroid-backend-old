from rest_framework import decorators, views, mixins, viewsets, response, generics
from django.db.models import F
from django.shortcuts import get_object_or_404
from . import models, serializers


class UserView(generics.RetrieveAPIView):
    queryset = models.User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = "username"


class FollowersListView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        user = get_object_or_404(models.User, username=username)
        return (
            user.followers.all()
            .values("follower__name", "follower__username")
            .annotate(name=F("follower__name"), username=F("follower__username"))
        )


class FollowingListView(generics.ListAPIView):
    serializer_class = serializers.UserSerializer

    def get_queryset(self):
        username = self.kwargs["username"]
        queryset = models.Follower.objects.filter(follower__username=username)
        return queryset.values("user__name", "user__username").annotate(
            name=F("user__name"), username=F("user__username")
        )
