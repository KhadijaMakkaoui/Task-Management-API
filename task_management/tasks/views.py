from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer, UserSerializer
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter

# Create your views here.
#CONTROLLER
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]  # Ensure user is logged in

    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['status', 'priority_level', 'due_date']  # Filtering fields
    ordering_fields = ['due_date', 'priority_level']  # Allow ordering by these fields
    ordering = ['due_date']  # Default ordering by due_date
    
    # return only the tasks that belong to the logged-in user
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the task
        serializer.save(user=self.request.user)
       
    def update_task(request, pk):
        task = get_object_or_404(Task, pk=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
#@action is used for custom actions that do not align with the standard CRUD operations. 
    @action(detail=True, methods=['patch'])
    def mark_complete(self):
        task = self.get_object()
        task.mark_complete()
        return Response({'status': 'Task marked as complete'})
    
    @action(detail=True, methods=['patch'])
    def mark_incomplete(self):
        task = self.get_object()
        task.mark_incomplete()
        return Response({'status': 'Task reverted to incomplete'})

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]