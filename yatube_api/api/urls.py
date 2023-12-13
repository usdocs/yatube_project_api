from django.urls import include, path
from rest_framework import routers

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

v1_router = routers.DefaultRouter()
v1_router.register(r'posts', PostViewSet)
v1_router.register(r'groups', GroupViewSet)
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet,
                   basename=r'comment')
v1_router.register(r'follow', FollowViewSet,
                   basename=r'follow')

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('auth/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
