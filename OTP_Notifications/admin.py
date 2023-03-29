from django.contrib import admin
# import app models
from .models import OTP

# Register your models here.
@admin.register(OTP)
class OTPAdmin (admin.ModelAdmin):
    list_display = ('otp_pin', 'email', 'pin_duration', 'active')
    list_display_links = ('otp_pin', 'email')