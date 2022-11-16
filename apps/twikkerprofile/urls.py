from django.urls import path
from apps.twikkerprofile.views import twikkerprofile, edit_profile, unfollow_tweeker, followers, follows, \
    follow_tweeker, toggle_dark_mode

urlpatterns = [
    path('u/<str:username>', twikkerprofile, name='twikkerprofile'),
    path('editprofile/', edit_profile, name='edit_profile'),
    path('u/<str:username>/follow/', follow_tweeker, name='follow_tweeker'),
    path('u/<str:username>/unfollow/', unfollow_tweeker, name='unfollow_tweeker'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('u/<str:username>/follows/', follows, name='follows'),
    path('settings/darkmode/', toggle_dark_mode, name='darkmode'),
]