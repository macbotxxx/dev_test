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
def send_email_func(email):
    """Sending email notification"""

    send_mail(
            'Subject here',
            'testing out new things using docker and celery and deploying it to the docker server',
            f'{email}',
            ['to@example.com'],
            fail_silently=False,
            )
    return "Done"


@celery_app.task()
def test_email_notification():
    """Sending email notification"""

    send_mail(
            'Subject here',
            'this is a scheduled notification using celery and await time',
            'user@example.com',
            ['to@example.com'],
            fail_silently=False,
            )
    return "Done"
