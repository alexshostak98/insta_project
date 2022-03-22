from rest_framework import routers

from .views.follower import FollowerViewSet


api_router = routers.DefaultRouter()

api_router.register('follower', FollowerViewSet)
