"""
from django.test import TestCase
from django.test import TestCase
from rest_framework.test import APIClient
# Create your tests here
class ChatbotAPITest(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_chatbot_response(self):
        response = self.client.post("/api/chatbot/chat/", {"message": "How do I cook jollof rice?"}, format="json")
        self.assertEqual(response.status_code, 200)
        print(response.json())  






"""
from django.test import TestCase
from .models import Recipe
import time

class RecipeQueryPerformanceTest(TestCase):
    def test_recipe_query_speed(self):
        start_time = time.time()
        Recipe.objects.filter(name__icontains="Rice")
        end_time = time.time()
        execution_time = end_time - start_time
        self.assertLess(execution_time, 0.5)  
"""