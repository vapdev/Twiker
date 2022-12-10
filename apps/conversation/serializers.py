from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import ConversationMessage, Conversation


class ChatSerializer(serializers.ModelSerializer):
    avatar_url = serializers.CharField(source='created_by.twikkerprofile.avatar.url')
    tweeker_name = serializers.CharField(source='created_by.twikkerprofile.user.username')

    class Meta:
        model = ConversationMessage
        fields = ['id', 'content', 'tweeker_name', 'created_at', 'avatar_url', 'formatted_time']


class ConversationSerializer(serializers.ModelSerializer):
    username = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    formatted_time = serializers.SerializerMethodField()

    def get_user_id(self, obj):
        user1 = obj.users.all()[0]
        user2 = obj.users.all()[1]
        user = self.context['request'].user
        if user == user1:
            return user2.id
        return user1.id

    def get_username(self, obj):
        user1 = obj.users.all()[0]
        user2 = obj.users.all()[1]
        print("users are", user1.username)
        user = self.context['request'].user
        print("user is", user)
        if user == user1:
            return user2.username
        return user1.username

    def get_formatted_time(self, obj):
        return naturaltime(obj.modified_at)

    class Meta:
        model = Conversation
        fields = ['id', 'username', 'formatted_time', 'user_id']

    