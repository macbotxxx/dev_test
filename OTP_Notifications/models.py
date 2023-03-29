from django.db import models
from datetime import timedelta, datetime
from django.utils import timezone


# Create your models here.

class OTP (models.Model):
    otp_pin = models.CharField(
        verbose_name="OTP Pin",
        max_length=6,
        null=True,
        help_text="This field store the OTP pin for verification"
    )

    email = models.EmailField(
        verbose_name="Email",
        null=True,
        help_text="this is the user email that will be used during the verification"
    )

    pin_duration = models.DateTimeField(
        verbose_name="OTP pin duration",
        default=timezone.now,
        null=True,
        help_text="this holds the duration for the pin sent to the user email"
    )

    active = models.BooleanField(
        verbose_name="Active",
        default=True,
        null=True,
        help_text="this is the user's active status for the otp verification"
    )

    def __str__(self):
        return str(self.email)
    
    def save(self, *args, **kwargs):
        self.pin_duration += timedelta(minutes=5)
        super(OTP, self).save(*args, **kwargs)
    

    