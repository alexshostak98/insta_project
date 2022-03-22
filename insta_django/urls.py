"""insta_django URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from publication_app.views import main_page, add_publication_page
from user_app.views import registration_page, authorization_page, profile_page, edit_profile_page
from hashtag_app.views import tag_page
from drf_spectacular.views import SpectacularRedocView, SpectacularSwaggerView, SpectacularAPIView
from hashtag_app.api.router import api_router as hashtags_router
from publication_app.api.router import api_router as posts_router
from media_app.api.router import api_router as media_router
from like_app.api.router import api_router as like_router
from comment_app.api.router import api_router as comment_router
from user_app.api.router import api_router as user_router
from follower_app.api.router import api_router as follower_router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_page),
    path('add-publication/', add_publication_page),
    path('registration/', registration_page),
    path('authorization/', authorization_page),
    path('profile/', profile_page),
    path('edit-profile/', edit_profile_page),
    path('tag/<str:hashtag>/', tag_page),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/redoc/', SpectacularRedocView.as_view(), name='redoc'),
    path('api/swagger/', SpectacularSwaggerView.as_view(), name='swagger-ui'),

    path('', include(posts_router.urls)),
    path('', include(hashtags_router.urls)),
    path('', include(media_router.urls)),
    path('', include(like_router.urls)),
    path('', include(comment_router.urls)),
    path('', include(user_router.urls)),
    path('', include(follower_router.urls)),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
