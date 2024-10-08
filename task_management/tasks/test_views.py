from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from tasks.models import Task, User
from django.contrib.auth import get_user_model

class TaskTests(APITestCase):

    def setUp(self):
        # Create a user for testing
        self.user = User.objects.create_user(
            username='testuser',
            password='testpass'
        )
        # Obtain JWT token for the user
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpass'
        })
        self.token = response.data['access']  # Get the access token
        
    def test_create_task(self):
        """
        Ensure we can create a new task.
        """
        url = reverse('task-list')
        data = {'title': 'Test Task', 'description': 'Task description', 'due_date': '2024-10-10', 'priority_level': 'high', 'status': 'pending'}
        # Include the token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Task.objects.count(), 1)
        self.assertEqual(Task.objects.get().title, 'Test Task')

    def test_get_task_list(self):
        """
        Ensure we can retrieve a list of tasks.
        """
        Task.objects.create(title='Test Task', description='Task description', due_date='2024-10-10', priority_level='high', status='pending', user=self.user)
        url = reverse('task-list')
        # Include the token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)

    def test_update_task(self):
        """
        Ensure we can update a task.
        """
        task = Task.objects.create(title='Test Task', description='Task description', due_date='2024-10-10', priority_level='high', status='pending', user=self.user)
        url = reverse('task-detail', kwargs={'pk': task.pk})
        data = {'title': 'Updated Task', 'description': 'Updated description', 'due_date': '2024-10-15', 'priority_level': 'medium', 'status': 'completed'}
        # Include the token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.title, 'Updated Task')
        self.assertEqual(task.status, 'completed')

    def test_delete_task(self):
        """
        Ensure we can delete a task.
        """
        task = Task.objects.create(title='Test Task', description='Task description', due_date='2024-10-10', priority_level='high', status='pending', user=self.user)
        url = reverse('task-detail', kwargs={'pk': task.pk})
        # Include the token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Task.objects.count(), 0)

    def test_task_mark_complete(self):
        """
        Ensure a task can be marked as complete.
        """
        task = Task.objects.create(title='Test Task', description='Task description', due_date='2024-10-10', priority_level='high', status='pending', user=self.user)
        url = reverse('task-mark-complete', kwargs={'pk': task.pk})
        # Include the token in the Authorization header
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + self.token)
        response = self.client.patch(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task.refresh_from_db()
        self.assertEqual(task.status, 'completed')
    
User = get_user_model()

class UserTests(APITestCase):

    def setUp(self):
        # Create a user for authentication
        self.user = User.objects.create_user(username='testuser', password='testpassword')

    def test_user_login(self):
        # Obtain a JWT token for the user
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'testpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Should return 200 OK
        self.assertIn('access', response.data)  # Check if the access token is in the response

    def test_user_login_invalid_credentials(self):
        # Attempt to log in with invalid credentials
        response = self.client.post(reverse('token_obtain_pair'), {
            'username': 'testuser',
            'password': 'wrongpassword'
        })
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Should return 401 Unauthorized