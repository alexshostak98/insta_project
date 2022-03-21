from rest_framework import routers

from .views.like import LikeViewSet


api_router = routers.DefaultRouter()

api_router.register('likes', LikeViewSet)
