from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from apps.twikkerprofile.models import TwikkerProfile


class TwikkerProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    followed_by = serializers.IntegerField(source='followed_by.count', read_only=True)
    following = serializers.IntegerField(source='follows.count', read_only=True)
    avatar = serializers.SerializerMethodField('get_avatar_url')
    
    def get_avatar_url(self, twikker_profile):
        if twikker_profile.avatar:
            return twikker_profile.avatar.url.replace('image/upload/', '')
        return None
    
    class Meta:
        model = TwikkerProfile
        fields = '__all__'