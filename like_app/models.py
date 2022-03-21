from django.db import models
from django.contrib.auth.models import User
from publication_app.models import Post


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='like')

    class Meta:
        unique_together = (('user', 'post'),)
