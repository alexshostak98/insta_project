from publication_app.models import Post
from comment_app.models import Comment

from django.dispatch import receiver
from .models import HashTag
from django.db.models.signals import post_save
import re


@receiver(post_save, sender=Comment)
@receiver(post_save, sender=Post)
def create_hashtag(sender, instance, *args, **kwargs):
    for title in re.findall(r"#([^\s]+)", instance.text):
        hashtag, created = HashTag.objects.get_or_create(title=title)
        hashtag.post.add(instance) if instance is Post else hashtag.comment.add(instance)
