from django.urls import path
from . import views  # ✅ Import views properly
from django.shortcuts import render
from django.http import HttpResponse
from .views import signup, verify_email


# Function to render the login page
def login_page(request):
    return render(request, "login.html")

urlpatterns = [
    path('', views.home, name='home'),
    path("", render, {"template_name": "index.html"}, name="home"),  # Homepage
    path("login/", login_page, name="login"),  # Login page
    path("signup/", lambda request: render(request, "signup.html"), name="signup"),#signup page
    path("signup/", signup, name="signup"),
    path("verify-email/<uidb64>/<token>/", verify_email, name="verify_email"),
]

