from django.dispatch import receiver
from django.db.models.signals import post_delete

from .models import Post


@receiver(post_delete, sender=Post)
def delete_profile_photo(sender, instance, **kwargs):
    instance.photo.delete(False)
