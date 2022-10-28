from django.urls import path

from apps.feed import consumers

websocket_urlpatterns = [
    path('ws/tweek/', consumers.TweekConsumer.as_asgi()),
    path('ws/like/', consumers.LikeConsumer.as_asgi()),
    path('ws/dislike/', consumers.DislikeConsumer.as_asgi()),
]