
"""
# Create your tests here.
from django.test import TestCase
from django.contrib.auth import get_user_model

class UserModelTest(TestCase):
    def test_create_user(self):
        User = get_user_model()
        user = User.objects.create_user(email='test@example.com', password='securepassword')
        self.assertEqual(user.email, 'test@example.com')
        self.assertTrue(user.check_password('securepassword'))


from rest_framework.test import APITestCase
from rest_framework import status

class UnauthorizedAccessTest(APITestCase):
    def test_protected_recipe_access(self):
        response = self.client.get('/api/recipes/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  














from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth import get_user_model

class AuthenticationAPITest(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = get_user_model().objects.create_user(email="testuser@example.com", password="SecurePass123")
        self.login_url = "/api/auth/login/"
        self.logout_url = "/api/auth/logout/"

    def test_successful_login(self):
        # Send a POST request with valid login credentials
        data = {"email": "testuser@example.com", "password": "SecurePass123"}
        response = self.client.post(self.login_url, data, format="json")

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Ensure request was successful
        self.assertIn("token", response.data)  # Ensure a token is returned

    def test_unsuccessful_login(self):
        # Send a POST request with incorrect credentials
        data = {"email": "testuser@example.com", "password": "WrongPassword"}
        response = self.client.post(self.login_url, data, format="json")

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)  # Ensure unauthorized response
        self.assertIn("error", response.data)  # Ensure error message is returned

    def test_successful_logout(self):
        # First, log in the user
        login_data = {"email": "testuser@example.com", "password": "SecurePass123"}
        login_response = self.client.post(self.login_url, login_data, format="json")
        token = login_response.data.get("token")

        # Authenticate the user by setting the token in the request headers
        self.client.credentials(HTTP_AUTHORIZATION=f"Token {token}")

        # Send a POST request to logout
        response = self.client.post(self.logout_url)

        # Assertions
        self.assertEqual(response.status_code, status.HTTP_200_OK)  # Ensure logout was successful
        self.assertIn("message", response.data)  # Ensure success message is returned
"""