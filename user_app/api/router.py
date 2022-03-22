from rest_framework import routers

from .views.user import UsersViewSet


api_router = routers.DefaultRouter()

api_router.register('users', UsersViewSet)
