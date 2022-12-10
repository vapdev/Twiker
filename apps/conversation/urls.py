from django.urls import path
from apps.conversation.views import conversations, conversation, global_chat, api_add_message, api_get_global_messages, \
    api_get_dm_messages, ConversationsList

urlpatterns = [
    path('api/conversations/', ConversationsList.as_view(), name='conversations'),
    path('conversation/<int:user_id>', conversation, name='conversation'),
    path('global/', global_chat, name='global'),
    path('api/add_message/', api_add_message, name='api_add_message'),
    path('api/messages/global/', api_get_global_messages, name='api_get_global_messages'),
    path('api/messages/<int:conversation_id>/', api_get_dm_messages, name='api_get_dm_messages'),
]