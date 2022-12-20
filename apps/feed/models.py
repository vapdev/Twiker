from django.db import models

from django.contrib.auth.models import User

from django.contrib.humanize.templatetags.humanize import naturaltime

class Tweek(models.Model):
    # A tweek is a post made by a user
    body = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='tweeks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # A tweek can be a reply to another tweek
    retweek = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.SET_NULL, related_name='retweeks')
    # A tweek can also be a comment on another tweek
    comment_from = models.ForeignKey('self', null=True, blank=True, default=None, related_name='comments', on_delete=models.SET_NULL)

    class Meta:
        ordering = ('-created_at',)
        unique_together = 'id', 'retweek'

    def formatted_time(self):
        return naturaltime(self.created_at)

class Like(models.Model):
    tweek = models.ForeignKey(Tweek, related_name='likes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='likes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = 'created_by', 'tweek'

class Dislike(models.Model):
    tweek = models.ForeignKey(Tweek, related_name='dislikes', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, related_name='dislikes', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = 'created_by', 'tweek'
