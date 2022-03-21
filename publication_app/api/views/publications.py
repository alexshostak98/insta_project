from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework import filters
from rest_framework.viewsets import GenericViewSet
from ..serializers.publications import PostSerializer
from ...models import Post


class PostsView(GenericViewSet, ListModelMixin, CreateModelMixin):
    serializer_class = PostSerializer
    queryset = Post.objects.filter(is_public=True)
    filter_backends = [filters.OrderingFilter, filters.SearchFilter]
    ordering_fields = ['create_date', 'id']
    ordering = ['-create_date']
    search_fields = ['hashtag__title']
