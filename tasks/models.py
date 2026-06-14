from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Task(models.Model):
    priority_choices = (
        ('low','low'),
        ('high','high')
    )
    
    status_choices = (
        ('pending', 'pending'),
        ('completed', 'completed')
    )
    
    reminder_choices = (
        (0, "at exact Time"),
        (5, "5 Minutes Before"),
        (10, "10 Minutes Before"),
        (15, "15 Minutes Before"),
        (20, "20 Minutes Before"),
        (30, "30 Minutes Before"),
    )
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    
    due_date = models.DateField()
    due_time = models.TimeField()

    priority = models.CharField(max_length=20, choices=priority_choices, default='high') 
    
    reminder_before = models.PositiveBigIntegerField(default=0, help_text='Reminder time in minutes before task', choices=reminder_choices)
    
    is_reminded = models.BooleanField(default=False)
    
    alarm_enabled = models.BooleanField(default=True)
    
    status = models.CharField(max_length=15,choices=status_choices, default='pending')
    
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    def __str__(self):
        return self.title


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)