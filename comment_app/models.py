from django.db import models
from django.contrib.auth.models import User
from publication_app.models import Post


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comment')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comment')
    text = models.TextField(max_length=1000, null=False, blank=True)
