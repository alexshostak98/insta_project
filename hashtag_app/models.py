from django.db import models
from publication_app.models import Post
from comment_app.models import Comment


class HashTag(models.Model):
    post = models.ManyToManyField(Post, related_name='hashtag')
    comment = models.ManyToManyField(Comment, related_name='hashtag')
    title = models.CharField(max_length=30, unique=True, null=False, blank=False)
