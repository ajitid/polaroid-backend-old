from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save

from .models import Post


@receiver(post_delete, sender=Post)
def delete_post_photo(sender, instance, **kwargs):
    instance.photo.delete(save=False)
    # FIXME deleting thumbnail
    # instance.thumbnail.delete(save=False)
