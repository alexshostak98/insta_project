from rest_framework.mixins import ListModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.hashtags import HashTagSerializer
from ...models import HashTag


class HashTagsView(GenericViewSet, ListModelMixin):
    serializer_class = HashTagSerializer
    queryset = HashTag.objects.all()
