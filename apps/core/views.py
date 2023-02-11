from rest_framework import generics
from django.views.decorators.csrf import csrf_exempt

from django.contrib.auth.models import User

from .serializers import UserSerializer
from django.contrib.auth import logout
from django.http import JsonResponse

@csrf_exempt

def logout_view(request):
    logout(request)
    return JsonResponse({'message': 'Logged out successfully'}, status=200)

class UsersList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        return User.objects.all()