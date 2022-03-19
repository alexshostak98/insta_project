from django.db import models
from django.contrib.auth.models import User

from django.core.validators import RegexValidator


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=False, related_name="profile")
    avatar = models.ImageField(null=True, blank=True)
    phone = models.CharField(
        max_length=16,
        validators=(
            RegexValidator(regex=r"^\+?\d{8,15}$", message="Wrong phone number"),
        ),
        blank=True,
        null=False,
    )
    bio = models.TextField(null=False, blank=True)
    github = models.URLField(max_length=2048, null=False, blank=True)
