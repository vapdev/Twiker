import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view

from apps.feed.models import Tweek

from apps.notification.utilities import create_notification
from .models import Conversation, ConversationMessage
from .serializers import ChatSerializer


@login_required
def api_add_message(request):
    data = json.loads(request.body)
    content = data['content']
    conversation_id = data['conversation_id']

    message = ConversationMessage.objects.create(conversation_id=conversation_id, content=content, created_by=request.user)

    if conversation_id:
        for user in message.conversation.users.all():
            if user != request.user:
                create_notification(request, user, 'message')

    return JsonResponse({'success': True})

@login_required
@api_view(['GET'])
def api_get_global_messages(request):
    messages = ConversationMessage.objects.filter(conversation_id=None).order_by('-created_at')
    # messages = messages[::-1]
    print("messages", messages)
    serializer = ChatSerializer(messages, many=True)
    return JsonResponse({'success': True, 'messages': serializer.data})