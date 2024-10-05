from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email']
    
class TaskSerializer(serializers.ModelSerializer):
    # Assign automatically based on the logged-in user
    user = UserSerializer(read_only=True)  
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority_level', 'status', 'user', 'completed_at']