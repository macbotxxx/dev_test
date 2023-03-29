# import user model
from django.contrib.auth import get_user_model
# import Django Packages
from django.core.mail import send_mail
# import celery
from config import celery_app
from celery import shared_task

# user model
User = get_user_model()


@celery_app.task()
def send_otp_email_func( email , otp_pin ):
    """Sending email notification"""
    send_mail(
            'OTP Verification',
            f'this is your otp pin for email verification, pin :: {otp_pin}',
            f'{email}',
            ['to@example.com'],
            fail_silently=False,
            )
    return "Done"