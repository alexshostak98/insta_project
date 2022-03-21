from rest_framework.mixins import ListModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.hashtags import HashTagSerializer, HashTagDetailSerializer
from ...models import HashTag


class HashTagsViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = HashTagSerializer
    queryset = HashTag.objects.all()
    action_serializers = {'retrieve': HashTagDetailSerializer}

    def get_serializer_class(self):
        return self.action_serializers.get(self.action, self.serializer_class)
