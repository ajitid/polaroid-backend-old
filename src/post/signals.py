from django.dispatch import receiver
from django.db.models.signals import post_delete, pre_save

from .models import Post


@receiver(post_delete, sender=Post)
def delete_post_photo(sender, instance, **kwargs):
    instance.photo.delete(save=False)
    # FIXME deleting thumbnail
    # https://github.com/matthewwithanm/django-imagekit/issues/229#issuecomment-385145019
    # instance.thumbnail.delete(save=False) <- this won't work, atleast not now
