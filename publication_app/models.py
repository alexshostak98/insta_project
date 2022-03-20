from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.PROTECT, related_name='post')
    title = models.CharField(max_length=256, unique=False, blank=True, null=False)
    image = models.ImageField(null=False, blank=False)
    create_date = models.DateTimeField(auto_now_add=True)
    is_public = models.BooleanField(default=True)
    text = models.TextField(blank=True, null=False)
