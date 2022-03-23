from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet
from ..serializers.user import UserSerializer, ProfileSerializer, CreateUserSerializer
from django.contrib.auth.models import User
from ...models import Profile
from publication_app.models import Post
from publication_app.api.serializers.publications import PostSerializer


class UsersViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin, CreateModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [filters.OrderingFilter, ]
    ordering_fields = ['date_joined', 'id']
    ordering = ['-date_joined']
    actions_serializers = {'retrieve': ProfileSerializer, 'create': CreateUserSerializer}

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)

    @action(methods=['get', ], detail=True, serializer_class=PostSerializer)
    def followings_posts(self, request, pk, *args, **kwargs):
        posts = Post.objects.filter(user__followers__follower=pk).order_by('-create_date').all()
        return Response(self.get_serializer(posts, many=True).data)

    @action(methods=['get', ], detail=True, serializer_class=UserSerializer)
    def followers(self, request, pk, *args, **kwargs):
        followers = User.objects.filter(followings__following=pk).all()
        return Response(self.get_serializer(followers, many=True).data)

    @action(methods=['get', ], detail=True, serializer_class=UserSerializer)
    def followings(self, request, pk, *args, **kwargs):
        followings = User.objects.filter(followers__follower=pk).all()
        return Response(self.get_serializer(followings, many=True).data)
