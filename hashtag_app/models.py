from django.db import models
from publication_app.models import Post


class HashTag(models.Model):
    post = models.ManyToManyField(Post, related_name='hashtag')
    title = models.CharField(max_length=30, unique=True, null=False, blank=False)
