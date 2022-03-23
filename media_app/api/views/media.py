from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.media import MediaSerializer
from ...models import Media


class MediaViewSet(GenericViewSet, CreateModelMixin, RetrieveModelMixin):
    serializer_class = MediaSerializer
    queryset = Media.objects.all()
