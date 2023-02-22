from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime
from cloudinary import CloudinaryResource
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
    avatar = serializers.SerializerMethodField()

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

    def get_avatar(self, obj):
        users = obj.users.all()
        user_count = users.count()
        if user_count == 2:
            user1 = obj.users.all().first()
            user2 = obj.users.all()[1]
            user = self.context['request'].user
            if user == user1:
                avatar_resource = user2.twikkerprofile.avatar
            else:
                avatar_resource = user1.twikkerprofile.avatar
            if isinstance(avatar_resource, CloudinaryResource):
                return str(avatar_resource.url)
            return None

    class Meta:
        model = Conversation
        fields = ['id', 'username', 'modified_at', 'user_id', 'avatar']

    