from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class Conversation(models.Model):
    user = user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='conversations')
    name = models.TextField(max_length=50)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Conversation by {self.user.username} at {self.created_at}"


class Messages(models.Model):
    message = models.TextField(max_length=500)
    conversation = models.ForeignKey(
        Conversation, on_delete=models.CASCADE, related_name='message')
    ai_message = models.TextField(max_length=5000)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"messages by {self.conversation.name} at {self.message}"
