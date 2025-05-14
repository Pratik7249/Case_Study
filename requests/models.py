from django.db import models
from accounts.models import User

class ServiceRequest(models.Model):
    REQUEST_CHOICES = [
        ('GAS_LEAK', 'Gas Leak'),
        ('INSTALLATION', 'Installation'),
        ('MAINTENANCE', 'Maintenance'),
    ]
    STATUS_CHOICES = [
        ('SUBMITTED', 'Submitted'),
        ('IN_PROGRESS', 'In Progress'),
        ('RESOLVED', 'Resolved'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    request_type = models.CharField(max_length=20, choices=REQUEST_CHOICES)
    description = models.TextField()
    attachment = models.FileField(upload_to='attachments/', blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='SUBMITTED')
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.request_type} - {self.status} ({self.user.username})"
