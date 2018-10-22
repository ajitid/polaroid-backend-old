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
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to=get_post_media_path)
    caption = models.CharField(max_length=180, blank=True, default="")
    posted = models.DateTimeField(_("posted on"), auto_now_add=True)

    class Meta:
        ordering = ["-posted"]

    def __str__(self):
        return gettext(f"{self.user.name} uploaded a post on {self.posted}")


class PostLike(models.Model):
    post = models.ForeignKey(Post, related_name="likes", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return gettext(f"{self.user.name} liked a post of {self.post.user.name}")


class PostComment(models.Model):
    post = models.ForeignKey(Post, related_name="comments", on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=180)

    def __str__(self):
        return gettext(f"{self.user.name} commented on a post of {self.post.user.name}")
