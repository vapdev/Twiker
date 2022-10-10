from django.contrib.auth.models import User
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from .models import Conversation, ConversationMessage

@login_required
def conversations(request):
    conversations = request.user.conversations.all()

    return render(request, 'conversation/conversations.html', {'conversations': conversations})

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

    return render(request, 'conversation/conversation.html', {'conversation': conversation})