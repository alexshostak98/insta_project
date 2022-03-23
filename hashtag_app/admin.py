from django.contrib import admin

from .models import HashTag


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    model = HashTag
