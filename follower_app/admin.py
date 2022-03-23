from django.contrib import admin
from .models import Follower


@admin.register(Follower)
class FollowerAdmin(admin.ModelAdmin):
    model = Follower
