from django.db import models


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
    

    
    
    