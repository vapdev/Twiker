from rest_framework import serializers

from .models import Tweek

class TweekSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tweek
        fields = ('id', 'body', 'created_by')