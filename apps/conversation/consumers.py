import json

from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async, async_to_sync
from django.contrib.auth.models import User
from django.utils import timezone

from .models import ConversationMessage, Conversation
from ..notification.utilities import create_notification


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        # Extract the `conversation_id` from the URL
        self.conversation_id = self.scope['url_route']['kwargs'].get('conversation_id')
        # Join the room using the `conversation_id`
        if self.conversation_id:
            await self.channel_layer.group_add(f'conversation_{self.conversation_id}', self.channel_name)
        elif self.conversation_id == 0:
            await self.channel_layer.group_add('global', self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        # Leave the room
        if self.conversation_id:
            await self.channel_layer.group_discard(f'conversation_{self.conversation_id}', self.channel_name)
        else:
            await self.channel_layer.group_discard('global', self.channel_name)

    async def receive(self, text_data):
        data = json.loads(text_data)
        content = data['content']
        tweeker_name = data['tweeker_name']
        avatar_url = data['avatar_url']

        to_user_id = await self.save_message(tweeker_name, self.conversation_id, content)

        # Send message to the room group
        if self.conversation_id:
            await self.channel_layer.group_send(
                f'conversation_{self.conversation_id}',
                {
                    'type': 'chat_message',
                    'content': content,
                    'tweeker_name': tweeker_name,
                    'avatar_url': avatar_url,
                    'conversation_id': self.conversation_id,
                }
            )
        else:
            await self.channel_layer.group_send(
                'global',
                {
                    'type': 'chat_message',
                    'content': content,
                    'tweeker_name': tweeker_name,
                    'avatar_url': avatar_url,
                    'conversation_id': self.conversation_id,
                }
            )

    async def chat_message(self, event):
        content = event['content']
        tweeker_name = event['tweeker_name']
        avatar_url = event['avatar_url']
        conversation_id = event['conversation_id']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'content': content,
            'tweeker_name': tweeker_name,
            'created_at': timezone.now().isoformat(),
            'avatar_url': avatar_url,
            'conversation_id': conversation_id
        }))

    @sync_to_async
    def save_message(self, tweeker_username, conversation_id, content):
        tweeker = User.objects.get(username=tweeker_username)
        try:
            conversation = Conversation.objects.get(id=conversation_id)
        except:
            conversation = None
        if not conversation:
            ConversationMessage.objects.create(created_by=tweeker, content=content)
        else:
            ConversationMessage.objects.create(created_by=tweeker, conversation=conversation, content=content)
            users = conversation.users.all()
            for user in users:
                if user != tweeker:
                    create_notification(created_by=tweeker, to_user=user, notification_type='message')
                    return user.id

