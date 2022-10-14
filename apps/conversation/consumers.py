import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from django.contrib.auth.models import User

from .models import ConversationMessage, Conversation


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Join room
        await self.channel_layer.group_add('global', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room
        await self.channel_layer.group_discard(
            'global',
            self.channel_name
        )

    # Receive message from web socket
    async def receive(self, text_data):
        print("PAS22SING")
        data = json.loads(text_data)
        content = data['content']
        tweeker = data['tweeker']
        created_at = 'Now'
        avatar = data['avatar']
        try:
            room = data['conversation']
        except:
            room = None

        await self.save_message(tweeker, room, content)

        # Send message to room group
        await self.channel_layer.group_send(
            'global',
            {
                'type': 'chat_message',
                'content': content,
                'tweeker': tweeker,
                'created_at': created_at,
                'avatar': avatar
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        print("PA2SSING")
        content = event['content']
        tweeker = event['tweeker']
        created_at = event['created_at']
        avatar = event['avatar']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'content': content,
            'tweeker': tweeker,
            'created_at': created_at,
            'avatar': avatar
        }))

    @sync_to_async
    def save_message(self, tweeker_username, conversation_id, content):
        print("PASSING")
        tweeker= User.objects.get(username=tweeker_username)
        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except:
            conversation = None
        ConversationMessage.objects.create(created_by=tweeker, conversation=conversation, content=content)
