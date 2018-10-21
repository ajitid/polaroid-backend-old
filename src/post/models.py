from django.db import models
from django.utils.translation import gettext_lazy as _, gettext

from user.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    photo = models.ImageField(width_field=640, height_field=640)
    caption = models.CharField(max_length=180)
    posted = models.DateTimeField(_("posted on"), auto_now_add=False)

    def __str__(self):
        return gettext(f"{self.user.name} uploaded a post on {self.posted}")


class PostLike(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return gettext(f"{self.user.name} liked a post of {self.post.user.name}")


class PostComment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=180)

    def __str__(self):
        return gettext(f"{self.user.name} commented on a post of {self.post.user.name}")
