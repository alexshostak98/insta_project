from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.viewsets import GenericViewSet
from ..serializers.publications import PostSerializer, PostDetailSerializer
from ...models import Post
from rest_framework.response import Response
from rest_framework.decorators import action


class PostsViewSet(GenericViewSet, ListModelMixin, CreateModelMixin, RetrieveModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['create_date', 'id']
    ordering = ['-create_date']
    search_fields = ['hashtag__title']
    actions_serializers = {'retrieve': PostDetailSerializer}

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)

    @action(methods=['get', ], detail=True, name='like_users')
    def like_users(self, request, pk, *args, **kwargs):
        instance = self.get_queryset().get(pk=pk)
        return Response(self.get_serializer(instance.like.all(), many=True).data)
