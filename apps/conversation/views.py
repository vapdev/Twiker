from django.shortcuts import render
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from apps.notification.utilities import create_notification
from .models import Conversation, ConversationMessage
from .serializers import ChatSerializer


@login_required
def conversations(request):
    conversations = request.user.conversations.all()

    return render(request, 'conversation/conversations.html', {'conversations': conversations})


@login_required
def global_chat(request):
    return render(request, 'conversation/global.html')


@login_required
def conversation(request, user_id):
    conversations = Conversation.objects.filter(users__in=[request.user.id])
    conversations = conversations.filter(users__in=[user_id])

    if conversations.count() == 1:
        conversation = conversations.first()
    else:
        recipient = User.objects.get(pk=user_id)
        conversation = Conversation.objects.create()
        conversation.users.add(request.user)
        conversation.users.add(recipient)
        conversation.save()

    return render(request, 'conversation/conversation.html', {'conversation': conversation, 'messages': conversation.messages.all()})


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
    messages = ConversationMessage.objects.filter(conversation_id=None).order_by('created_at')
    serializer = ChatSerializer(messages, many=True)
    return JsonResponse({'success': True, 'messages': serializer.data})


@login_required
@api_view(['GET'])
def api_get_dm_messages(request, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    messages = conversation.messages.all().order_by('created_at')
    serializer = ChatSerializer(messages, many=True)
    return JsonResponse({'success': True, 'messages': serializer.data})

