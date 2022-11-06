from django.db import models

from django.contrib.auth.models import User


class Conversation(models.Model):
    users = models.ManyToManyField(User, related_name='conversations')
    modified_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-modified_at']


class ConversationMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE, null=True)
    content = models.TextField()
    created_by = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']

    def save(self, *args, **kwargs):
        if self.conversation:
            self.conversation.save()

        super(ConversationMessage, self).save(*args, **kwargs)

    def formatted_time(self):
        return self.created_at.strftime(' %d/%m %H:%M:%S')