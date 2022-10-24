import json
import re

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.contrib.auth.models import User

from apps.feed.api import save_like, save_tweek
from apps.feed.models import Tweek
from apps.notification.models import Notification
from apps.notification.utilities import create_notification


class TweekConsumer(AsyncWebsocketConsumer):

    async def connect(self):
        # Join room
        await self.channel_layer.group_add('tweek', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            'tweek',
            self.channel_name
        )

    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        body = data['body']
        tweeker = data['tweeker']

        await save_tweek(body=body, tweeker=tweeker)

        await self.channel_layer.group_send(
            'tweek',
            {
                'type': 'tweek_message',
                'body': body,
                'tweeker': tweeker,
            }
        )


    # Receive message from room group
    async def tweek_message(self, event):
        body = event['body']
        tweeker = event['tweeker']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'body': body,
            'tweeker': tweeker,
        }))


class LikeConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room
        await self.channel_layer.group_add('like', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            'like',
            self.channel_name
        )

    # Receive message from web socket
    async def receive(self, text_data):
        data = json.loads(text_data)
        tweek_id = data['tweek_id']
        liker = data['liker']

        await save_like(tweek_id=tweek_id, liker=liker)

        await self.channel_layer.group_send(
            'like',
            {
                'type': 'like_message',
                'tweek_id': tweek_id,
                'liker': liker,
            }
        )

    # Receive message from room group
    async def like_message(self, event):
        tweek_id = event['tweek_id']
        liker = event['liker']
        tweek_owner = await self.get_tweek_owner(tweek_id=tweek_id)
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'tweek_id': tweek_id,
            'liker': liker,
            'tweek_owner': tweek_owner.username,
        }))

    @sync_to_async
    def get_tweek_owner(self, tweek_id):
        tweek = Tweek.objects.get(pk=tweek_id)
        return tweek.created_by