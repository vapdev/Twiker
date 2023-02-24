from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import Tweek, Like


class TweekSerializer(serializers.ModelSerializer):
    tweeker_name = serializers.CharField(source='created_by')
    likes_count = serializers.IntegerField(source='likes.count')
    dislikes_count = serializers.IntegerField(source='dislikes.count')
    retweek_count = serializers.IntegerField(source='retweeks.count')
    avatar_url = serializers.CharField(source='created_by.twikkerprofile.avatar')
    image = serializers.CharField(allow_null=True)

    is_liked = serializers.SerializerMethodField()
    is_disliked = serializers.SerializerMethodField()
    is_retweek = serializers.SerializerMethodField()
    is_retweeked = serializers.SerializerMethodField()

    retweek_avatar_url = serializers.CharField(source='retweek.created_by.twikkerprofile.avatar', allow_null=True)
    retweek_tweeker_name = serializers.CharField(source='retweek.created_by', allow_null=True)
    retweek_body = serializers.CharField(source='retweek.body', allow_null=True)
    retweek_likes_count = serializers.IntegerField(source='retweek.likes.count', allow_null=True)
    retweek_dislikes_count = serializers.IntegerField(source='retweek.dislikes.count', allow_null=True)
    retweek_retweek_count = serializers.IntegerField(source='retweek.retweeks.count', allow_null=True)
    retweek_avatar_url = serializers.CharField(source='retweek.created_by.twikkerprofile.avatar', allow_null=True)
    retweek_created_at = serializers.CharField(source='retweek.created_at', allow_null=True)
    retweek_id = serializers.IntegerField(source='retweek.id', allow_null=True)
    retweek_image = serializers.CharField(source='retweek.image', allow_null=True)

    reply_parent_tweeker_name = serializers.CharField(source='comment_from.created_by', allow_null=True)

    is_retweek_liked = serializers.SerializerMethodField()
    is_retweek_disliked = serializers.SerializerMethodField()

    def get_is_liked(self, obj):
        user = self.context['request'].user
        return obj.likes.filter(created_by=user).exists()

    def get_is_disliked(self, obj):
        user = self.context['request'].user
        return obj.dislikes.filter(created_by=user).exists()

    def get_is_retweeked(self, obj):
        user = self.context['request'].user
        return obj.retweeks.filter(created_by=user).exists()

    def get_is_retweek(self, obj):
        if obj.retweek:
            return True
        return False

    def get_is_retweek_liked(self, obj):
        user = self.context['request'].user
        if obj.retweek:
            return obj.retweek.likes.filter(created_by=user).exists()
        return None

    def get_is_retweek_disliked(self, obj):
        user = self.context['request'].user
        if obj.retweek:
            return obj.retweek.dislikes.filter(created_by=user).exists()
        return None

    class Meta:
        model = Tweek
        fields = ('id', 'body', 'created_by', 'image', 'tweeker_name', 'likes_count', 'dislikes_count', 'avatar_url',
                  'created_at', 'retweek', 'comment_from', 'reply_parent_tweeker_name', 'retweek_tweeker_name', 'retweek_likes_count', 'retweek_dislikes_count',
                  'retweek_avatar_url', 'retweek_created_at', 'retweek_image', 'retweek_body', 'retweek_id', 'retweek_count',
                  'retweek_retweek_count', 'is_liked', 'is_disliked', 'is_retweeked', 'is_retweek', 'is_retweek_liked', 'is_retweek_disliked', 'retweeks')