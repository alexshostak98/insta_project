from rest_framework import serializers
from ...models import HashTag


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        fields = ['title']


class HashTagDetailSerializer(HashTagSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'
