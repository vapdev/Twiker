from django.urls import path

from apps.twikkerprofile import consumers

websocket_urlpatterns = [
    path('ws/follow/', consumers.FollowConsumer.as_asgi()),
]