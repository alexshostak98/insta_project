from rest_framework import serializers
from django.contrib.auth.models import User
from ...models import Profile
from publication_app.api.serializers.publications import PostSerializer


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'
        read_only_fields = ['user']

    publisher_user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(),
        source='user'
    )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'post', 'profile']

    # profile = ProfileSerializer(allow_null=False, read_only=True)
    post = PostSerializer(many=True, allow_null=True, read_only=True)
