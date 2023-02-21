from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import ConversationMessage, Conversation


class ChatSerializer(serializers.ModelSerializer):
    avatar_url = serializers.CharField(source='created_by.twikkerprofile.avatar')
    tweeker_name = serializers.CharField(source='created_by.twikkerprofile.user.username')

    class Meta:
        model = ConversationMessage
        fields = ['id', 'content', 'tweeker_name', 'created_at', 'avatar_url']


class ConversationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        users = obj.users.all()
        user_count = users.count()
        if user_count == 2:
            user1 = obj.users.all().first()
            user2 = obj.users.all()[1]
            user = self.context['request'].user
            if user == user1:
                return user2.id
            return user1.id

    def get_username(self, obj):
        users = obj.users.all()
        user_count = users.count()
        if user_count == 2:
            user1 = obj.users.all().first()
            user2 = obj.users.all()[1]
            user = self.context['request'].user
            if user == user1:
                return user2.username
            return user1.username

    class Meta:
        model = Conversation
        fields = ['id', 'username', 'modified_at', 'user_id']

    