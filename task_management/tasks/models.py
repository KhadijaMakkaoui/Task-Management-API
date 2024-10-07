from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model):
    PRIORITY_CHOICES=[
        ('low', 'Low'),
        ('medium', 'Medium'),
        ('high', 'High'),
    ]
    
    STATUS_CHOICES =[
        ('pending', 'Pending'),
        ('completed', 'Completed'),
    ]
    title = models.CharField(max_length=255)
    description = models.TextField()
    due_date = models.DateField()
    priority_level= models.CharField(max_length=10, choices=PRIORITY_CHOICES)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='pending')
    
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    completed_at = models.DateTimeField(null=True, blank=True)
    
    #TO mark task's status as completed
    def mark_complete(self):
        self.status = 'completed'
        self.completed_at = timezone.now()
        self.save()
    
    #To mark task's status as pending
    def mark_incomplete(self):
        self.status = 'pending'
        self.completed_at = None
        self.save()

    #show task title
    def __str__(self):
        return self.title
    
    #Validation to check due date
    def validate_date(self):
        if self.due_date < timezone.now().date():
            raise Exception('Due date must be in the future.')
    
    
    
    