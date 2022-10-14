from django import template
register = template.Library()


@register.simple_tag
def get_chat_user_id(conversation, request_user):
    users = conversation.users.all()
    for user in users:
        if user != request_user:
            return user.id
