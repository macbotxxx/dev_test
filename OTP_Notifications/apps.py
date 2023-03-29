from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class OtpNotificationsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'OTP_Notifications'
    verbose_name = _('OTP Notifications')
