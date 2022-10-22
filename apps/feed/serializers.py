from rest_framework import serializers

from .models import Tweek

class TweekSerializer(serializers.ModelSerializer):
    tweeker_name = serializers.CharField(source='created_by')

    class Meta:
        model = Tweek
        fields = ('id', 'body', 'created_by', 'tweeker_name')