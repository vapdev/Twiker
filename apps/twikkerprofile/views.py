import json

from asgiref.sync import sync_to_async
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.models import User
from rest_framework.decorators import api_view
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from apps.notification.utilities import create_notification
from apps.twikkerprofile.serializers import TwikkerProfileSerializer
from cloudinary import uploader

from .forms import TwikkerProfileForm
from ..core.serializers import UserSerializer
from ..notification.models import Notification
from .models import TwikkerProfile

@permission_classes((IsAuthenticated, ))
@api_view(['POST'])
def toggle_dark_mode(request):
    data = request.data
    user_id = data['user_id']
    user = User.objects.get(id=user_id)
    user.twikkerprofile.dark_mode = not user.twikkerprofile.dark_mode
    user.twikkerprofile.save()
    return JsonResponse({'dark_mode': user.twikkerprofile.dark_mode})

@permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def get_user_data(request, username):
    user = get_object_or_404(User, username=username)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)

@permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def get_profile_data(request, username):
    user = get_object_or_404(User, username=username)
    profile = user.twikkerprofile
    serializer = TwikkerProfileSerializer(profile)
    return JsonResponse(serializer.data)

@permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def get_auth_user(request):
    user = get_object_or_404(User, username=request.user.username)
    serializer = UserSerializer(user)
    return JsonResponse(serializer.data)


@permission_classes((IsAuthenticated, ))
@api_view(['POST'])
def unfollow_tweeker(request, username):
    user = get_object_or_404(User, username=username)

    request.user.twikkerprofile.follows.remove(user.twikkerprofile)
    return JsonResponse({'success': True})


@permission_classes((IsAuthenticated, ))
@api_view(['POST'])
def follow_tweeker(request, username):
    user = get_object_or_404(User, username=username)

    request.user.twikkerprofile.follows.add(user.twikkerprofile)
    return JsonResponse({'success': True})


@permission_classes((IsAuthenticated, ))
@api_view(['GET'])
def user1_follows_user2(request, username1, username2):
    user1 = get_object_or_404(User, username=username1)
    user2 = get_object_or_404(User, username=username2)
    return JsonResponse({'follows': user1.twikkerprofile.follows.filter(user=user2).exists()})

@permission_classes((IsAuthenticated, ))
@api_view(['POST'])
def update_avatar(request):
    user = request.user
    image = request.FILES.get('file', None)
    if image:
        result = uploader.upload(image, upload_preset="ml_default")
        image_url = result['secure_url']
        profile = TwikkerProfile.objects.get(user=user)
        profile.avatar = image_url
        profile.save()
    else:
        image_url = None
    return JsonResponse({'success': True})