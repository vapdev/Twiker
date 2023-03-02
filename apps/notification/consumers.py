import json
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from channels.layers import get_channel_layer
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.serializers.json import DjangoJSONEncoder
from asgiref.sync import async_to_sync
from ..feed.models import Tweek
from ..feed.serializers import TweekSerializer

class TweekConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.user_id = self.scope['url_route']['kwargs']['user_id']
        self.group_name = f'timeline_{self.user_id}'
        await self.channel_layer.group_add(self.group_name, self.channel_name)
        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(self.group_name, self.channel_name)

    async def receive(self, text_data):
        pass
    
    async def send_tweek(self, event):
        # Extract the tweek ID from the event data
        tweek_id = event['tweek']
        
        # Fetch the tweek object from the database
        tweek = await database_sync_to_async(Tweek.objects.get)(id=tweek_id)
        
        # Convert the tweek object to a dictionary
        tweek_dict = {
            'id': tweek.id,
            'content': tweek.body,
        }

        # Serialize the tweek object to JSON
        tweek_json = json.dumps(tweek_dict, cls=DjangoJSONEncoder)
        
        # Construct a message containing the tweek data
        message = {
            'type': 'send_tweek',
            'tweek': tweek_json,
        }
        
        # Send the message to the WebSocket client
        await self.send(text_data = json.dumps(message))


@receiver(post_save, sender=Tweek)
def notify_followers(sender, instance, **kwargs):
    # Get the list of followers of the tweek's author
    followers = instance.author_followers()
    channel_layer = get_channel_layer()

    # For each follower, send a notification via WebSocket
    for follower in followers:
        # Get the channel group name for the follower
        group_name = f'timeline_{follower.id}'   
        # Send a message to the follower's channel group
        async_to_sync(channel_layer.group_send)(
            group_name,
            {'type': 'send_tweek', 'tweek': instance.id}
        )
