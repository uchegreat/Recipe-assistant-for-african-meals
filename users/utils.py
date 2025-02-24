from django.core.mail import send_mail
from django.conf import settings
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str
from django.template.loader import render_to_string
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth import get_user_model
from django.urls import reverse

User = get_user_model()

def send_verification_email(user, request):
    token = default_token_generator.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))

    verification_link = request.build_absolute_uri(
        reverse("verify_email", kwargs={"uidb64": uid, "token": token})
    )

    subject = "Confirm Your Recipe Assistant Account"
    message = render_to_string("emails/verification_email.html", {"user": user, "verification_link": verification_link})

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])
