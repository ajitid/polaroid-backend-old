from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from django.shortcuts import get_object_or_404

from user.serializers import UserSerializer
from . import models, views


class PostSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")
    name = serializers.ReadOnlyField(source="user.name")
    likes = serializers.ReadOnlyField(source="likes.count")

    class Meta:
        model = models.Post
        fields = ("username", "name", "photo", "caption", "timestamp", "likes")
        extra_kwargs = {
            "timestamp": {"read_only": True},
            "url": {"view_name": "posts:post-detail", "lookup_field": "id"},
        }

    def create(self, validated_data):
        user = self.context["request"].user
        post = models.Post.objects.create(user=user, **validated_data)
        return post


class PostWithUrlSerializer(PostSerializer):
    class Meta(PostSerializer.Meta):
        fields = ("url", "username", "name", "photo", "caption", "timestamp", "likes")


class PostPhotoOnlySerializer(serializers.ModelSerializer):
    post = serializers.HyperlinkedIdentityField(view_name="posts:post-detail", lookup_field="id")

    class Meta(PostSerializer.Meta):
        model = models.Post
        fields = ("photo", "post")


# TODO
#  def save(self):
#     user = CurrentUserDefault()  # <= over self.context['request'].user
#            ^^^ but this didn't worked on create()
#     title = self.validated_data['title']
#     article = self.validated_data['article']


class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = models.Comment
        fields = ("username", "comment")

    def create(self, validated_data):
        post_id = self.context["post_id"]
        post = get_object_or_404(models.Post, id=post_id)
        user = self.context["request"].user
        comment = models.Comment.objects.create(user=user, post=post, **validated_data)
        return comment
