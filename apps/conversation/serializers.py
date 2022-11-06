from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import ConversationMessage


class ChatSerializer(serializers.ModelSerializer):
    avatar_url = serializers.CharField(source='created_by.twikkerprofile.avatar.url')
    tweeker_name = serializers.CharField(source='created_by.twikkerprofile.user.username')

    class Meta:
        model = ConversationMessage
        fields = ['id', 'content', 'tweeker_name', 'created_at', 'avatar_url', 'formatted_time']

