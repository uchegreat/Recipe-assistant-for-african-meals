"""from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.shortcuts import get_object_or_404
import openai
from django.conf import settings
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeImageGenerationView(APIView):
    def post(self, request, *args, **kwargs):
        meal_name = request.data.get("prompt", "").strip().lower()

        allowed_meals = [
            "jollof rice", "egusi soup", "fufu", "bobotie", "piri piri chicken",
            "suya", "injera", "waakye", "maafe", "nshima", "nyama choma",
            "moin moin", "thieboudienne", "chakalaka", "ugali", "bunny chow"
        ]

        if meal_name not in allowed_meals:
            return Response({"error": "Sorry, image generation is only available for African meals."})

        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

        response = client.images.generate(
            model="dall-e-3",
            prompt=f"A delicious plate of {meal_name}, a traditional African dish, beautifully plated",
            size="1024x1024",
            quality="standard"
        )

        image_url = response.data[0].url

        return Response({"image_url": image_url})"
"""