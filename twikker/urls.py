"""twikker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views

from apps.conversation.views import conversations, conversation, global_chat
from apps.core.views import frontpage, signup, users
from apps.feed.views import api_get_profile_tweeks, api_remove_like, api_delete_tweek, api_get_tweeks, api_remove_dislike, \
    api_remove_retweek, api_add_like, api_add_dislike, api_add_tweek, api_get_tweek
from apps.feed.views import feed, search, view_tweek
from apps.notification.views import notifications, clear_notifications
from apps.twikkerprofile.views import twikkerprofile, edit_profile, unfollow_tweeker, followers, follows, \
    follow_tweeker, toggle_dark_mode
from apps.conversation.views import api_add_message, api_get_global_messages, api_get_dm_messages

from apps.notification.views import NotificationsList

urlpatterns = [
    #
    #

    path('cornelios/', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),

    #
    #


    path('', feed, name='feed'),
    path('tweek/<int:tweek_id>/', view_tweek, name='view_tweek'),
    path('search/', search, name='search'),
    path('u/<str:username>', twikkerprofile, name='twikkerprofile'),
    path('editprofile/', edit_profile, name='edit_profile'),
    path('notifications/', notifications, name='notifications'),
    path('clear_notifications/', clear_notifications, name='clear_notifications'),
    path('conversations/', conversations, name='conversations'),
    path('global/', global_chat, name='global'),
    path('users/', users, name='users'),
    path('conversation/<int:user_id>', conversation, name='conversation'),
    path('u/<str:username>/follow/', follow_tweeker, name='follow_tweeker'),
    path('u/<str:username>/unfollow/', unfollow_tweeker, name='unfollow_tweeker'),
    path('u/<str:username>/followers/', followers, name='followers'),
    path('u/<str:username>/follows/', follows, name='follows'),

    #
    #
    # API
    path('api/add_tweek/', api_add_tweek, name='api_add_tweek'),
    path('api/delete_tweek/', api_delete_tweek, name='api_delete_tweek'),
    path('api/add_like/', api_add_like, name='remove_like'),
    path('api/remove_like/', api_remove_like, name='remove_like'),
    path('api/add_dislike/', api_add_dislike, name='remove_dislike'),
    path('api/remove_dislike/', api_remove_dislike, name='remove_dislike'),
    path('api/remove_retweek/', api_remove_retweek, name='remove_retweek'),
    path('api/add_message/', api_add_message, name='api_add_message'),
    path('api/get_tweeks/', api_get_tweeks, name='get_tweeks'),
    path('api/get_profile_tweeks/<int:user_id>/', api_get_profile_tweeks, name='get_profile_tweeks'),
    path('api/messages/global/', api_get_global_messages, name='api_get_global_messages'),
    path('api/messages/<int:conversation_id>/', api_get_dm_messages, name='api_get_dm_messages'),
    path('api/tweek/<int:tweek_id>/', api_get_tweek, name='api_get_tweek'),
    path('api/notifications/<int:user_id>', NotificationsList.as_view(), name='api_get_notifications'),


    path('settings/darkmode/', toggle_dark_mode, name='darkmode'),

    #
    #
    # Admin

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
