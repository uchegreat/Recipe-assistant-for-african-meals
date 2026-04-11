from django.contrib.auth import get_user_model
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import uuid
from .serializers import RegisterSerializer
from .utils import send_verification_email
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.models import User

User = get_user_model()

# Store verification tokens
verification_tokens = {}

# User Registration View
@api_view(['POST'])
def register_user(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        user = serializer.save()
        token = str(uuid.uuid4())  # Generate unique verification token
        verification_tokens[token] = user.id  # Store token

        print(f"🔎 Debug: User {user.username} - Email: {user.email}")  # Debugging
        send_verification_email(user, token)  # Send verification email

        return Response({'message': 'User registered successfully. Check your email to verify your account.'}, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Email Verification View
@api_view(['GET'])
def verify_email(request, token):
    user_id = verification_tokens.get(token)

    if user_id:
        user = User.objects.get(id=user_id)
        user.is_verified = True
        user.save()
        del verification_tokens[token]  # Remove token after verification
        return Response({'message': 'Email verified successfully. You can now log in.'}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid or expired token'}, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt  #  Disable CSRF protection for this API
@api_view(['POST'])
def login_user(request):
    username = request.data.get('username')
    password = request.data.get('password')

    user = authenticate(username=username, password=password)

    if user:
        if not user.is_verified:
            return Response({'error': 'Account not verified. Check your email.'}, status=status.HTTP_403_FORBIDDEN)

        token, created = Token.objects.get_or_create(user=user)

        return Response({'message': 'Login successful', 'token': token.key}, status=status.HTTP_200_OK)

    return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)