from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _, gettext


class User(AbstractUser):
    email = models.EmailField(_("email address"))
    first_name = None
    last_name = None
    name = models.CharField(_("name"), max_length=50)

    def get_short_name(self):
        if not self.name:
            return ""
        name_with_abbr = self.name[0 : self.name.rfind(".") + 1]
        if name_with_abbr:
            return name_with_abbr
        return self.name.split()[0]

    class Meta(AbstractUser.Meta):
        pass


"""
class Profile(models.Model):
    bio, dob, dp, private_account
"""


class Follower(models.Model):
    user = models.ForeignKey(User, related_name="followers", on_delete=models.CASCADE)
    follower = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "follower"),)

    def __str__(self):
        return gettext(f"{self.user} has follower {self.follower}")


class BlockedUser(models.Model):
    user = models.ForeignKey(User, related_name="blocked_users", on_delete=models.CASCADE)
    blocked_user = models.ForeignKey(User, related_name="+", on_delete=models.CASCADE)

    class Meta:
        unique_together = (("user", "blocked_user"),)

    def __str__(self):
        return gettext(f"{self.user} has blocked user f{self.blocked_user}")
