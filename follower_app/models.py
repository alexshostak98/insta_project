from django.db import models
from django.contrib.auth.models import User


class Follower(models.Model):
    follower = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='followings')
    following = models.ForeignKey(User, null=False, blank=False, on_delete=models.CASCADE, related_name='followers')

    class Meta:
        unique_together = ('follower', 'following')
