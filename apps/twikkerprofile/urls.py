from django.urls import path
from apps.twikkerprofile.views import unfollow_tweeker, follow_tweeker, \
toggle_dark_mode, get_user_data, get_profile_data, get_auth_user, update_avatar, user1_follows_user2

urlpatterns = [
    path('u/<str:username>/follow/', follow_tweeker, name='follow_tweeker'),
    path('u/<str:username>/unfollow/', unfollow_tweeker, name='unfollow_tweeker'),
    path('settings/darkmode/', toggle_dark_mode, name='darkmode'),
    path('api/user_data/<str:username>', get_user_data, name='get_user_data'),
    path('api/profile_data/<str:username>', get_profile_data, name='get_profile_data'),
    path('api/auth_user/', get_auth_user, name='get_user_data'),
    path('api/follow/<str:username>', follow_tweeker, name='follow'),
    path('api/unfollow/<str:username>', unfollow_tweeker, name='unfollow'),
    path('api/update_avatar/', update_avatar, name='update_avatar'),
    path('api/user1_follows_user2/<str:username1>/<str:username2>', user1_follows_user2, name='user1_follows_user2'),
]