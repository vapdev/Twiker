from datetime import datetime
from rest_framework import serializers
from django.contrib.humanize.templatetags.humanize import naturaltime

from apps.twikkerprofile.models import TwikkerProfile


class TwikkerProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = TwikkerProfile
        fields = '__all__'