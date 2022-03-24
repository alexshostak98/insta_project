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

    def validate_post(self, value):
        if value in self.context.get('request').user.post.all():
            raise serializers.ValidationError("You can't like your posts")
        return value


class LikeCommentSerializer(LikeSerializer):
    class Meta:
        model = Like
        exclude = ['post']
        read_only_fields = ['user']

    def validate_comment(self, value):
        if value in self.context.get('request').user.comment.all():
            raise serializers.ValidationError("You can't like your comments")
        return value
