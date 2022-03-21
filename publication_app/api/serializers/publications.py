from rest_framework import serializers
from ...models import Post
from media_app.api.serializers.media import MediaSerializer
from hashtag_app.api.serializers.hashtags import HashTagSerializer


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['is_public']
        read_only_fields = ['user']
        extra_kwargs = {
            'file': {'required': True, 'write_only': True}
        }

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    media = MediaSerializer(source='file', allow_null=False, read_only=True)
    hashtag = HashTagSerializer(many=True, read_only=True)

    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, instance) -> int:
        return instance.like.count()
