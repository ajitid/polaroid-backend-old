from rest_framework import decorators, views, mixins, viewsets, response, generics
from rest_framework.permissions import IsAuthenticated
from django.db.models import F
from django.shortcuts import get_object_or_404, Http404
from . import models, serializers


class PostCreateView(generics.CreateAPIView):
    serializer_class = serializers.PostSerializer
    permission_classes = (IsAuthenticated,)


class PostDetailView(generics.RetrieveAPIView):
    queryset = models.Post.objects.all()
    serializer_class = serializers.PostSerializer
    lookup_field = "id"
