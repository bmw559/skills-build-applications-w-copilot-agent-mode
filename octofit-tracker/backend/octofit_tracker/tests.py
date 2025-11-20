from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import User, Team, Activity, Leaderboard, Workout

class UserTests(APITestCase):
    def test_create_user(self):
        url = reverse('user-list')
        data = {'name': 'Test User', 'email': 'test@example.com', 'team': 'Alpha'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class TeamTests(APITestCase):
    def test_create_team(self):
        url = reverse('team-list')
        data = {'name': 'Alpha', 'members': []}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class ActivityTests(APITestCase):
    def test_create_activity(self):
        url = reverse('activity-list')
        data = {'user_email': 'test@example.com', 'activity': 'Running', 'duration': 30}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LeaderboardTests(APITestCase):
    def test_create_leaderboard(self):
        url = reverse('leaderboard-list')
        data = {'team': 'Alpha', 'points': 100}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class WorkoutTests(APITestCase):
    def test_create_workout(self):
        url = reverse('workout-list')
        data = {'name': 'Push Ups', 'description': 'Do 20 push ups'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
