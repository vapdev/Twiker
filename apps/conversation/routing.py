from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/global/', consumers.ChatConsumer.as_asgi()),
]