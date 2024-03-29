from .models import Notification


def create_notification(created_by, to_user, notification_type):
    notification = Notification.objects.create(to_user=to_user, notification_type=notification_type,
                                               created_by=created_by)
    return notification

def create_notification_bulk(notifications):
    notification = Notification.objects.bulk_create(notifications)
    return notification
