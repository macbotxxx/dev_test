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
    """
    Sending email notification , this is a task that will be executed
    after 15 seconds by sneding email to the users and notifying them about the 
    new api update that will be available soon.
    """

    send_mail(
            'Update Kroon Network V2 API',
            'this is to imform you that from so and soo day that the v1 API wont be available again , kindly start migrating to v2 for better performance.',
            'user@example.com',
            ['to@example.com'],
            fail_silently=False,
            )
    return "Notification is published"
