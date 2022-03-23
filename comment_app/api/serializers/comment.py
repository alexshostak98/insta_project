from rest_framework import serializers
from ...models import Comment


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )

    likes_count = serializers.SerializerMethodField()

    def get_likes_count(self, instance) -> int:
        return instance.like.count()
