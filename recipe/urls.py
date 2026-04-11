"""
from django.urls import path
from .views import RecipeDetailView

urlpatterns = [
    path("api/recipes/<int:pk>/", RecipeDetailView.as_view(), name="recipe-detail"),
]
"""


