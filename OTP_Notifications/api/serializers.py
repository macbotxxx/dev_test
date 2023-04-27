# import DRF package
from rest_framework import serializers
# import Custom Apps Models
from OTP_Notifications.models import OTP


class OTP_Serializer(serializers.ModelSerializer):

    class Meta:
        model = OTP
        fields = ('email',)

