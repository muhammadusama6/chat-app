from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    text = models.TextField(default='')
    seen = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    sender_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_messages')
    receiver_name = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_messages')