from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import PostViewSet, GroupViewSet
from .views import CommentViewSet, FollowViewSet


app_name = 'api'

router_v1 = DefaultRouter()
router_v1.register(r'posts/(?P<post_id>[^/.]+)/comments',
                   CommentViewSet, basename='comment')
router_v1.register('groups', GroupViewSet)
router_v1.register('posts', PostViewSet)
router_v1.register('follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]