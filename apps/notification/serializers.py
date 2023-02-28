from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from apps.notification.models import Notification
from apps.twikkerprofile.models import TwikkerProfile

class NotificationSerializer(serializers.ModelSerializer):
    avatar_url = serializers.SerializerMethodField()

    def get_avatar_url(self, obj):
        profile = TwikkerProfile.objects.get(user=obj.created_by)
        return profile.avatar
    

    class Meta:
        model = Notification
        fields = '__all__'