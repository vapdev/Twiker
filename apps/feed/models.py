from django.db import models

from django.contrib.auth.models import User

from django.contrib.humanize.templatetags.humanize import naturaltime

class Tweek(models.Model):
    body = models.CharField(max_length=255)
    created_by = models.ForeignKey(User, related_name='tweeks', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    retweek = models.ForeignKey('self', null=True, blank=True, default=None, on_delete=models.SET_NULL)
    retweeks = models.ManyToManyField('self', blank=True, related_name='retweeks')

    class Meta:
        ordering = ('-created_at',)

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