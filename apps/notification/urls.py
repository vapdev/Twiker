from django.urls import path
from apps.notification.views import notifications, clear_notifications, NotificationsList

urlpatterns = [
    path('notifications/', notifications, name='notifications'),
    path('clear_notifications/', clear_notifications, name='clear_notifications'),
    path('api/notifications/<int:user_id>', NotificationsList.as_view(), name='api_get_notifications'),
]