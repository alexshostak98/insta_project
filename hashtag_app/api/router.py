from rest_framework import routers

from .views.hashtags import HashTagsViewSet


api_router = routers.DefaultRouter()

api_router.register('hashtag', HashTagsViewSet)
