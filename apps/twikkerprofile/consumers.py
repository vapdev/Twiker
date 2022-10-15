import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

from apps.notification.models import Notification
from apps.notification.utilities import create_notification
from apps.twikkerprofile.views import save_follow


class FollowConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room
        await self.channel_layer.group_add('follow', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            'follow',
            self.channel_name
        )

    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        follower = data['follower']
        following = data['following']

        await save_follow(follower_id=follower, following_id=following)

        # Send message to room group
        await self.channel_layer.group_send(
            'follow',
            {
                'type': 'follow_message',
                'follower': follower,
                'following': following,
            }
        )

    # Receive message from room group
    async def follow_message(self, event):
        follower = event['follower']
        following = event['following']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'follower': follower,
            'following': following,
        }))

