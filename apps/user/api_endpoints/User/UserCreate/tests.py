import json
import os

from rest_framework import status
from django.core.files import File
from django.urls import reverse
from rest_framework.test import APITestCase

from apps.user.models import User


class UserCreateTest(APITestCase):
    def setUp(self):
        pass

    def test_user_create(self):
        url = reverse("user-create")
        data = {
            "username": "test",
            "first_name": "Test",
            "last_name": "Test1",
            "password1": "test1",
            "password2": "test1",
            "email": "user@gmail.com",
            "avatar": open("media/avatar.jpeg", "rb")
        }
        response = self.client.post(url, data)
        user = User.objects.get(id=1)
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 201)
        self.assertEqual(User.objects.count(), 1)
        self.assertEqual(data["username"], user.username)


class ForgotPasswordAPITest(APITestCase):
    def test_forgot_password(self):
        host_email = os.getenv("EMAIL_HOST_USER")
        url = reverse('forgot-password')
        data = {'email': host_email}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class ActivateUserAPITest(APITestCase):
    def test_activate_user(self):
        host_email = os.getenv("EMAIL_HOST_USER")
        user = User.objects.create(username='test_user', email=host_email)
        token = user.token
        url = reverse('user:reset-password', kwargs={'token': token})
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
