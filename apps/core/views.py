import os
from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
import requests
import json
from django.contrib.auth.models import User

from apps.core.models import Image

from .serializers import UserSerializer
from django.contrib.auth import logout
from django.http import JsonResponse
from cloudinary import uploader
import cloudinary
from django.conf import settings

cloudinary.config(
  cloud_name = settings.CLOUDINARY_CLOUD_NAME,
  api_key = settings.CLOUDINARY_API_KEY,
  api_secret = settings.CLOUDINARY_API_SECRET,
  secure = True
)

@csrf_exempt
def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'}, status=200)

class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()

class ImageViewSet(viewsets.ModelViewSet):
    
    @action(detail=False, methods=['post'])

    def upload_image(self, request):
        image = request.data['file']
        result = uploader.upload(image, upload_preset="ml_default")
        image_url = result['secure_url']
        Image.objects.create(image_url=image_url)
        return Response({'image_url': image_url})