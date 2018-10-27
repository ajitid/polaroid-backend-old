from uuid import uuid4
import os.path as path
from django.db import models
from django.utils.translation import gettext_lazy as _, gettext

from django.contrib.auth import get_user_model

User = get_user_model()


def get_post_media_path(instance, filename):
    name, ext = path.splitext(filename)
    return path.join("post-media", f"{instance.id}{ext}")


class Post(models.Model):
    id = models.UUIDField(_("post id"), primary_key=True, default=uuid4, editable=False, unique=True)
    user = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_post_media_path)
    caption = models.CharField(max_length=180, blank=True)
    timestamp = models.DateTimeField(_("posted on"), auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="likes", blank=True)

    class Meta:
        ordering = ["-timestamp"]

    def __str__(self):
        return gettext(f"{self.user.name} added a post on {self.timestamp}")


class Comment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=180)
    timestamp = models.DateTimeField(_("posted on"), auto_now_add=True)

    class Meta:
        ordering = ["timestamp"]

    def __str__(self):
        return gettext(f"{self.user.name} commented on a post of {self.post.user.name}")
