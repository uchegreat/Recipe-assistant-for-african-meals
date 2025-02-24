from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.contrib import messages
from .utils import send_verification_email  # Import email function
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import force_str

# ✅ Simple Login View
def login_view(request):
    return render(request, "login.html")

# ✅ Simple Signup View 
def signup(request):
    return render(request, "signup.html")

def home(request):
    return render(request, 'index.html')




User = get_user_model()

def signup(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        password = request.POST["password"]
        confirm_password = request.POST["confirm_password"]

        if password == confirm_password:
            if User.objects.filter(email=email).exists():
                messages.error(request, "Email already registered.")
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.is_active = False  # User is inactive until email is verified
                user.save()

                send_verification_email(user, request)  # ✅ Send email

                messages.success(request, "Account created! Please check your email to verify your account.")
                return redirect("login")
        else:
            messages.error(request, "Passwords do not match.")

    return render(request, "signup.html")


def verify_email(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True  # ✅ Activate user account
        user.save()
        messages.success(request, "Your account has been verified! You can now log in.")
        return redirect("login")
    else:
        messages.error(request, "Invalid or expired verification link.")
        return redirect("signup")

