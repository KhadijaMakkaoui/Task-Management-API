from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User


# Create your views here.
#CONTROLLER
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    # return only the tasks that belong to the logged-in user
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the task
        serializer.save(user=self.request.user)
       
#@action is used for custom actions that do not align with the standard CRUD operations. 
    @action(detail=True, methods=['patch'])
    def mark_complete(self, request, pk=None):
        task = self.get_object()
        task.mark_complete()
        return Response({'status': 'Task marked as complete'})
    
    @action(detail=True, methods=['patch'])
    def mark_incomplete(self, request, pk=None):
        task = self.get_object()
        task.mark_incomplete()
        return Response({'status': 'Task reverted to incomplete'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]