from rest_framework import serializers
from ...models import HashTag


class HashTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = HashTag
        exclude = ['post', 'comment']

    posts_count = serializers.SerializerMethodField()

    def get_posts_count(self, instance) -> int:
        return instance.post.count()


class HashTagDetailSerializer(HashTagSerializer):
    class Meta:
        model = HashTag
        fields = '__all__'
