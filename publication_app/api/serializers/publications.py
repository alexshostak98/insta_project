from rest_framework import serializers
from ...models import Post
from media_app.api.serializers.media import MediaSerializer


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
