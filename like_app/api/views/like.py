from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.like import LikePostSerializer, LikeCommentSerializer
from ...models import Like


# class LikeViewSet(GenericViewSet, CreateModelMixin):
#     serializer_class = LikeSerializer
#     queryset = Like.objects.all()


class LikePostViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = LikePostSerializer
    queryset = Like.objects.all()


class LikeCommentViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = LikeCommentSerializer
    queryset = Like.objects.all()
