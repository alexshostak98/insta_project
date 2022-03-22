from rest_framework import serializers
from ...models import Like


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class LikePostSerializer(LikeSerializer):
    class Meta:
        model = Like
        exclude = ['comment']
        read_only_fields = ['user']


class LikeCommentSerializer(LikeSerializer):
    class Meta:
        model = Like
        exclude = ['post']
        read_only_fields = ['user']
