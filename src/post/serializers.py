from rest_framework import serializers
from rest_framework.fields import CurrentUserDefault
from user.serializers import UserSerializer
from . import models, views


class PostSerializer(serializers.HyperlinkedModelSerializer):
    username = serializers.ReadOnlyField(source="user.username")

    class Meta:
        model = models.Post
        fields = ("username", "photo", "caption", "posted")
        extra_kwargs = {"posted": {"read_only": True}, "url": {"view_name": "posts:post-detail", "lookup_field": "id"}}

    def create(self, validated_data):
        user = self.context["request"].user
        post = models.Post.objects.create(user=user, **validated_data)
        return post


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
