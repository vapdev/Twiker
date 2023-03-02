from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import models


class UserSerializer(serializers.ModelSerializer):
    followed_by = serializers.IntegerField(source='twikkerprofile.followed_by.count', read_only=True)
    following = serializers.IntegerField(source='twikkerprofile.follows.count', read_only=True)
    avatar = serializers.CharField(source='twikkerprofile.avatar', read_only=True)
    dark_mode = serializers.BooleanField(source='twikkerprofile.dark_mode', read_only=True)
    biography = serializers.CharField(source='twikkerprofile.biography', read_only=True)
    profile_id = serializers.IntegerField(source='twikkerprofile.id', read_only=True)

    class Meta:
        model = User
        fields = '__all__'
