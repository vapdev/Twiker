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
from django.urls import path
from django.contrib.auth import views

from apps.conversation.views import conversations, conversation, global_chat
from apps.core.views import frontpage, signup, users
from apps.feed.api import api_add_tweek, api_add_like, api_remove_like, api_delete_tweek
from apps.feed.views import feed, search
from apps.notification.views import notifications
from apps.twikkerprofile.views import twikkerprofile, edit_profile, follow_tweeker, unfollow_tweeker, followers, follows
from apps.conversation.api import api_add_message

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
    path('search/', search, name='search'),
    path('u/<str:username>', twikkerprofile, name='twikkerprofile'),
    path('editprofile/', edit_profile, name='edit_profile'),
    path('notifications/', notifications, name='notifications'),
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
    path('api/add_like/', api_add_like, name='api_add_like'),
    path('api/remove_like/', api_remove_like, name='remove_like'),
    path('api/add_message/', api_add_message, name='api_add_message'),

    #
    #
    # Admin

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
