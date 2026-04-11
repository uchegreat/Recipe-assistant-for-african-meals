from django.urls import path
from .views import RecipeChatbotView

urlpatterns = [
    path("chat/", RecipeChatbotView.as_view(), name="chatbot"), 
]
