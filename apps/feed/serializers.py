from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from .models import Tweek, Like



class TweekSerializer(serializers.ModelSerializer):
    tweeker_name = serializers.CharField(source='created_by')
    likes_count = serializers.IntegerField(source='likes.count')
    dislikes_count = serializers.IntegerField(source='dislikes.count')
    avatar_url = serializers.CharField(source='created_by.twikkerprofile.avatar.url')

    retweek_tweeker_name = serializers.CharField(source='retweek.created_by', allow_null=True)
    retweek_body = serializers.CharField(source='retweek.body', allow_null=True)
    retweek_likes_count = serializers.IntegerField(source='retweek.likes.count', allow_null=True)
    retweek_dislikes_count = serializers.IntegerField(source='retweek.dislikes.count', allow_null=True)
    retweek_avatar_url = serializers.CharField(source='retweek.created_by.twikkerprofile.avatar.url', allow_null=True)
    retweek_formatted_time = serializers.CharField(source='retweek.formatted_time', allow_null=True)


    class Meta:
        model = Tweek
        fields = ('id', 'body', 'created_by', 'tweeker_name', 'likes_count', 'dislikes_count', 'avatar_url',
                  'formatted_time', 'retweek', 'retweek_tweeker_name', 'retweek_likes_count', 'retweek_dislikes_count',
                  'retweek_avatar_url', 'retweek_formatted_time', 'retweek_body')