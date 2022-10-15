import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from django.contrib.auth.models import User

from .models import ConversationMessage, Conversation
from ..notification.utilities import create_notification


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
        data = json.loads(text_data)
        content = data['content']
        tweeker = data['tweeker']
        created_at = 'Now'
        avatar = data['avatar']
        conversation = data['conversation_id']

        to_user_id = await self.save_message(tweeker, conversation, content)
        print("USERID", to_user_id)

        # Send message to room group
        await self.channel_layer.group_send(
            'global',
            {
                'type': 'chat_message',
                'content': content,
                'tweeker': tweeker,
                'created_at': created_at,
                'avatar': avatar,
                'to_user_id': to_user_id,
            }
        )

    # Receive message from room group
    async def chat_message(self, event):
        content = event['content']
        tweeker = event['tweeker']
        created_at = event['created_at']
        avatar = event['avatar']
        to_user_id = event['to_user_id']
        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'content': content,
            'tweeker': tweeker,
            'created_at': created_at,
            'avatar': avatar,
            'to_user_id': to_user_id,
        }))

    @sync_to_async
    def save_message(self, tweeker_username, conversation_id, content):
        tweeker= User.objects.get(username=tweeker_username)

        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except:
            conversation = None

        ConversationMessage.objects.create(created_by=tweeker, conversation=conversation, content=content)

        if conversation:

            users = conversation.users.all()

            for user in users:
                if user != tweeker:
                    create_notification(created_by=tweeker, to_user=user, notification_type='message')
                    return user.id


