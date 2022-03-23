from rest_framework import routers

from .views.like import LikePostViewSet, LikeCommentViewSet


api_router = routers.DefaultRouter()

api_router.register('likes/post', LikePostViewSet)
api_router.register('likes/comment', LikeCommentViewSet)

