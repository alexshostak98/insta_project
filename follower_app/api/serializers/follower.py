from rest_framework import serializers
from ...models import Follower


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = '__all__'
        read_only_fields = ['follower']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='follower'
    )
