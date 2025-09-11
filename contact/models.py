from django.db import models
from django.utils import timezone


class Contact(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=20, blank=True)

    def __str__(self):
        return self.name


class Message(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name="messages")
    service = models.CharField(max_length=100)
    message = models.TextField()
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.contact.name} - {self.timestamp.strftime('%Y-%m-%d %H:%M')}"


class UniqueContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100)
    message = models.TextField()
    subscribe = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('email', 'message')  # avoid redundancy

    def __str__(self):
        return f"{self.name} - {self.service} @ {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
