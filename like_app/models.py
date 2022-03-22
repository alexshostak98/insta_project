from django.db import models
from django.contrib.auth.models import User
from publication_app.models import Post
from comment_app.models import Comment


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=False, blank=False, related_name='like')
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=False, related_name='like')
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=False, related_name='like')

    class Meta:
        unique_together = (('user', 'post'), ('user', 'comment'))
