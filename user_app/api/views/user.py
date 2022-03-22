from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin
from rest_framework import filters
from rest_framework.viewsets import GenericViewSet
from ..serializers.user import UserSerializer, ProfileSerializer
from django.contrib.auth.models import User
from ...models import Profile


class UsersViewSet(GenericViewSet, ListModelMixin, RetrieveModelMixin):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    filter_backends = [filters.OrderingFilter, ]
    ordering_fields = ['date_joined', 'id']
    ordering = ['-date_joined']
    actions_serializers = {'retrieve': ProfileSerializer}

    def get_serializer_class(self):
        return self.actions_serializers.get(self.action, self.serializer_class)
