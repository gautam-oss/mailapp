from django.db import models
from django.contrib.auth.models import User


class SentEmail(models.Model):
    sender = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name="sent_emails")
    recipient = models.EmailField()
    subject = models.CharField(max_length=255)
    body = models.TextField()
    sent_at = models.DateTimeField(auto_now_add=True)
    success = models.BooleanField(default=True)

    class Meta:
        ordering = ["-sent_at"]

    def __str__(self):
        return f"{self.sender} → {self.recipient} ({self.sent_at:%Y-%m-%d %H:%M})"