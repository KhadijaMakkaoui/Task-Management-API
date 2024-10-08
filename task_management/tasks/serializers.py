from rest_framework import serializers
from django.contrib.auth.models import User
from .models import Task

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # Create a new user and set it to active
        # **validated_data:  It allows you to pass key-value pairs in a dictionary as keyword arguments to a function.
        user = User.objects.create_user(**validated_data)
        user.is_active = True  # Ensure the user is active
        user.save()
        return user
class TaskSerializer(serializers.ModelSerializer):
    # Assign automatically based on the logged-in user
    user = UserSerializer(read_only=True)  
    class Meta:
        model = Task
        fields = ['id', 'title', 'description', 'due_date', 'priority_level', 'status', 'user', 'completed_at']
    
    
    def validate(self, data):
        """Ensure completed tasks cannot be updated unless reverted to incomplete."""
        print(f"Current instance status: {self.instance.status if self.instance else 'No instance'}")
        print(f"New status: {data.get('status')}")
        # Check if the instance (task) exists, meaning it's an update operation
        if self.instance:
            # Get the current status from the database
            if self.instance.status == 'completed' and data.get('status') != 'pending':
                raise serializers.ValidationError("You cannot update a completed task unless you revert it to incomplete.")
        
        return data
