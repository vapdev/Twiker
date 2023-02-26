from django.urls import path

from . import consumers

websocket_urlpatterns = [
    path('ws/chat/', consumers.ChatConsumer.as_asgi()),
    path('ws/direct_chat/<int:id>/', consumers.ChatConsumer.as_asgi()),    

]