from django.shortcuts import render, redirect

from django.contrib.auth.decorators import login_required
from rest_framework import generics

from .models import Notification
from .serializers import NotificationSerializer


@login_required
def notifications(request):
    goto = request.GET.get('goto', '')
    notification_id = request.GET.get('notification', 0)

    if goto != '':
        notification = Notification.objects.get(pk=notification_id)
        notification.is_read = True
        notification.save()

        if notification.notification_type == Notification.MESSAGE:
            return redirect('conversation', user_id=notification.created_by.id)
        elif notification.notification_type == Notification.FOLLOWER:
            return redirect('twikkerprofile', username=notification.created_by.username)
        elif notification.notification_type == Notification.LIKE:
            return redirect('twikkerprofile', username=notification.to_user.username)
        elif notification.notification_type == Notification.MENTION:
            return redirect('twikkerprofile', username=notification.created_by.username)

    return render(request, 'notification/notifications.html')


@login_required
def clear_notifications(request):
    Notification.objects.filter(to_user=request.user).update(is_read=True)
    return redirect('notifications')


class NotificationsList(generics.ListAPIView):
    serializer_class = NotificationSerializer

    def get_queryset(self):
        return Notification.objects.filter(to_user=self.kwargs.get("user_id"))