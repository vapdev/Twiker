from django.urls import path
from apps.twikkerprofile.views import edit_profile, unfollow_tweeker, followers, follows, \
    follow_tweeker, toggle_dark_mode, get_user_data, get_auth_user

urlpatterns = [
    path('editprofile/', edit_profile, name='edit_profile'),
    path('u/<str:username>/follow/', follow_tweeker, name='follow_tweeker'),
    path('u/<str:username>/unfollow/', unfollow_tweeker, name='unfollow_tweeker'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('u/<str:username>/follows/', follows, name='follows'),
    path('settings/darkmode/', toggle_dark_mode, name='darkmode'),
    path('api/user_data/<str:username>', get_user_data, name='get_user_data'),
    path('api/auth_user/', get_auth_user, name='get_user_data'),
    path('api/follow/<str:username>', follow_tweeker, name='follow'),
    path('api/unfollow/<str:username>', unfollow_tweeker, name='unfollow'),
]