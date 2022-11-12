from django.contrib.auth.models import User
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    followed_by = serializers.IntegerField(source='twikkerprofile.followed_by.count', read_only=True)
    following = serializers.IntegerField(source='twikkerprofile.follows.count', read_only=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'followed_by', 'following']