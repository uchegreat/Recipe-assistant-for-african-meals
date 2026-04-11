from django.urls import path
from . import views  #  Import views properly
from django.shortcuts import render
from .views import register_user, verify_email, login_user

# Function to render the login page
def login_page(request):
    return render(request, "login.html")

urlpatterns = [
    path("", render, {"template_name": "index.html"}, name="home"),  # Homepage
    path("login/", login_page, name="login"),  # Login page
    path("signup/", lambda request: render(request, "signup.html"), name="signup"),#signup page 
    path('register/', register_user, name='register'),
    path('login/', login_user, name='login'),
    path('verify/<str:token>/', verify_email, name='verify_email'), 
]

