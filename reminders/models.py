from django.db import models
from django.utils import timezone


class Reminder(models.Model):
    """
    Model to store reminder information.
    """
    NOTIFICATION_CHOICES = (
        ('email', 'Email'),
        ('sms', 'SMS'),
    )
    
    STATUS_CHOICES = (
        ('pending', 'Pending'),
        ('sent', 'Sent'),
        ('failed', 'Failed'),
    )
    
    title = models.CharField(max_length=200, blank=True)
    message = models.TextField()
    reminder_date = models.DateField()
    reminder_time = models.TimeField()
    notification_method = models.CharField(
        max_length=10, 
        choices=NOTIFICATION_CHOICES,
        default='email'
    )
    recipient = models.CharField(max_length=100)
    status = models.CharField(
        max_length=10,
        choices=STATUS_CHOICES,
        default='pending'
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.title or 'Reminder'} on {self.reminder_date} at {self.reminder_time}"
    
    @property
    def is_due(self):
        """Check if reminder is due to be sent."""
        now = timezone.now()
        reminder_datetime = timezone.make_aware(
            timezone.datetime.combine(self.reminder_date, self.reminder_time)
        )
        return reminder_datetime <= now