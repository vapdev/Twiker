from django import template

from apps.conversation.models import Conversation

register = template.Library()


@register.simple_tag
def get_chat_user_id(conversation, request_user):
    users = conversation.users.all()
    for user in users:
        if user != request_user:
            return user.id


@register.simple_tag
def is_in_conv(user_id, conversation_id):
    conversation = Conversation.objects.get(pk=conversation_id)
    users = conversation.users.all()
    for user in users:
        if user.id == user_id:
            return True
    return False