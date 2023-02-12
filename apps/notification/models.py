from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    MESSAGE = 'message'
    FOLLOWER = 'follower'
    LIKE = 'like'
    DISLIKE = 'dislike'
    MENTION = 'mention'

    CHOICES = (
        (MESSAGE, 'Message'),
        (FOLLOWER, 'Follower'),
        (LIKE, 'Like'),
        (DISLIKE, 'Dislike'),
        (MENTION, 'Mention'),
    )

    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='notifications')

    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='creatednotifications')
    created_by_username = models.CharField(max_length=150)

    def save(self, *args, **kwargs):
        self.created_by_username = self.created_by.username
        super().save(*args, **kwargs)
    
    class Meta:
        ordering = ['-created_at']