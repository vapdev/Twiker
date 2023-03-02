from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/feed/<int:user_id>', consumers.TweekConsumer.as_asgi()),    
]