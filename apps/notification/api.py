from apps.notification.models import Notification
from .serializers import NotificationSerializer
from rest_framework import generics


class NotificationsList(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(to_user=self.kwargs.get("user_id"))



