from rest_framework import serializers
from django.contrib.auth.models import User
from ...models import Profile


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
        fields = ['id', 'username', 'post', 'profile', 'followings_count', 'followers_count', ]

    # profile = ProfileSerializer(allow_null=False, read_only=True)
    # post = PostSerializer(many=True, allow_null=True, read_only=True)

    followings_count = serializers.SerializerMethodField()
    followers_count = serializers.SerializerMethodField()

    def get_followings_count(self, instance) -> int:
        return instance.followings.count()

    def get_followers_count(self, instance) -> int:
        return instance.followers.count()


class CreateUserSerializer(UserSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user
