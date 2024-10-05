from django.shortcuts import render
from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.utils import timezone
from .models import Task
from .serializers import TaskSerializer
from rest_framework.permissions import IsAuthenticated
# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    # Queryset should return only the tasks that belong to the logged-in user
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)