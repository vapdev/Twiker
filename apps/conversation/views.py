from django.shortcuts import render
import json
from django.contrib.auth.models import User
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from apps.notification.utilities import create_notification
from .models import Conversation, ConversationMessage
from .serializers import ChatSerializer, ConversationSerializer



@api_view(['GET'])
@permission_classes((IsAuthenticated, ))
def api_get_conversation(request, user_id):
    print("request.user.id: ", request.user.id)
    print("user_id: ", user_id)
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

    return JsonResponse({'conversation_id': conversation.id})

@api_view(['POST'])
@permission_classes((IsAuthenticated, ))
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


@permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def api_get_messages(request, conversation_id):
    if conversation_id==0:
        messages = ConversationMessage.objects.filter(conversation_id=None).order_by('created_at')
    else:
        conversation = Conversation.objects.get(pk=conversation_id)
        messages = conversation.messages.all().order_by('created_at')
    serializer = ChatSerializer(messages, many=True)
    return JsonResponse({'success': True, 'messages': serializer.data})


class ConversationsList(generics.ListAPIView):
    serializer_class = ConversationSerializer

    def get_queryset(self):
        return self.request.user.conversations.all()