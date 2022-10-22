from rest_framework import serializers

from .models import Tweek

class TweekSerializer(serializers.ModelSerializer):
    tweeker_name = serializers.CharField(source='created_by')
    avatar_url = serializers.CharField(source='created_by.twikkerprofile.avatar.url')

    class Meta:
        model = Tweek
        fields = ('id', 'body', 'created_by', 'tweeker_name', 'avatar_url')