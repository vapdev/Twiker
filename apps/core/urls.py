from django.urls import path
from django.contrib.auth import views
from apps.core.views import ImageViewSet, logout_view, UsersList, FollowersList, FollowingList

urlpatterns = [
    path('api/v1/auth/logout/', logout_view, name='logout'),
    path('api/users/', UsersList.as_view(), name='api_get_users'),
    path('api/users/followers/<int:user_id>', FollowersList.as_view(), name='followers_list'),
    path('api/users/following/<int:user_id>', FollowingList.as_view(), name='following_list'),
    path('api/upload_image/', ImageViewSet.as_view({'post': 'upload_image'}), name='api_upload_image'),
]
