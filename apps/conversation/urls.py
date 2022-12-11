from django.urls import path
from apps.conversation.views import api_get_conversation, api_add_message, api_get_messages, ConversationsList

urlpatterns = [
    path('api/conversations/', ConversationsList.as_view(), name='conversations'),
    path('api/get_conversation/<int:user_id>/', api_get_conversation, name='conversations'),
    path('api/add_message/', api_add_message, name='api_add_message'),
    path('api/messages/<int:conversation_id>/', api_get_messages, name='api_get_dm_messages'),
]