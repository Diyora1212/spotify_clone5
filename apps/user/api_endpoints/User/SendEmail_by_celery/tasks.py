import os

from celery import shared_task
from django.core.mail import send_mail

from apps.user.models import User


@shared_task
def send_activation_email(email, activation_link):
    subject = 'Activate your account'
    user = User.objects.get(email=email)
    user.userprofile.email = email
    host_email = os.getenv("EMAIL_HOST_USER")
    message = f'Please click on the following link to activate your account: {activation_link}'
    send_mail(subject, message, (host_email,), [user.userprofile.email], fail_silently=False)
