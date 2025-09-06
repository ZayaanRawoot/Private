from django.db import models

class ContactMessage(models.Model):
    SERVICE_CHOICES = [
        ('cctv', 'CCTV Installation'),
        ('alarm', 'Alarm System'),
        ('access', 'Access Control'),
        ('monitoring', '24/7 Monitoring'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    service = models.CharField(max_length=100, choices=SERVICE_CHOICES)
    message = models.TextField()
    subscribe = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)  

    def __str__(self):
        return f"{self.name} - {self.service}"
    