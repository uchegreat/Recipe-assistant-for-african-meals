from django.core.mail import send_mail
from django.conf import settings

def send_verification_email(user, token):
    try:
        if not user.email:
            print("❌ ERROR: User does not have an email!")
            return
        
        subject = "Verify Your Email"
        message = f"Click the link to verify your account: http://127.0.0.1:8000/api/auth/verify/{token}/"
        
        print(f" Attempting to send email to: {user.email}")  # Debugging
        email_sent = send_mail(subject, message, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)

        if email_sent:
            print(f" Verification email sent successfully to: {user.email}")
        else:
            print(" Failed to send verification email.")

    except Exception as e:
        print(" Error while sending verification email:", e)


