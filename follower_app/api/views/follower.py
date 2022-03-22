from rest_framework.mixins import CreateModelMixin
from rest_framework.viewsets import GenericViewSet
from ..serializers.follower import FollowerSerializer
from ...models import Follower


class FollowerViewSet(GenericViewSet, CreateModelMixin):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
