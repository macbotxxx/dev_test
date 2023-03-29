# import
import random
import string
# import django packages
from django.utils import timezone
# import DRF packages
from rest_framework.generics import CreateAPIView , ListAPIView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
# import App Serializer
from .serializers import OTP_Serializer
# import task 
from OTP_Notifications.tasks import send_otp_email_func
# import app models 
from OTP_Notifications.models import OTP


def otp_pin_generator():
    return ''.join(random.choices(string.digits , k=6))
    # return ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))





class OPT_View ( CreateAPIView ):
    permission_classes = [ AllowAny,]
    serializer_class = OTP_Serializer
    queryset = OTP.objects.all()


    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data = request.data)
        if serializer.is_valid():
            # getting the validated data of email 
            email = serializer.validated_data.get('email')
            otp_pin = otp_pin_generator()
            # otp_pin.instance = otp_pin
            # checking if user is already saved
            verify = self.get_queryset().filter( email = email )
            if verify.exists():
                # deleting the old otp_pin
                verify.delete()
            # send otp to the user email address
            send_otp_email_func.delay( email = email , otp_pin = otp_pin )
            # save the validated data 
            serializer.save( otp_pin = otp_pin )

            return Response({'status':'successful', 'message':'Otp is sent to the user email address successfully', 'data':serializer.data}, status=status.HTTP_201_CREATED )
        
        return Response(serializer.error_messages, status=status.HTTP_400_BAD_REQUEST)





class OTP_Verification_View (ListAPIView):
    permission_classes = [ AllowAny,]
    serializer_class = OTP_Serializer
    queryset = OTP.objects.all()

    def get (self, request, *args, **kwargs):
        email = kwargs.get('email')
        otp_pin = kwargs.get('otp_pin')
        # checking for the pin duration 
        recent_time = timezone.now()

        verify = self.get_queryset().filter( email = email, otp_pin = otp_pin , active = True )
        if verify.exists():
            # for loop to get the pin duration
            for v in verify:
                pin_duration = v.pin_duration
                # checking the recent time and pin duration
                if recent_time > pin_duration:
                    # deleting the old otp_pin
                    verify.delete()
                    # returning the response
                    return Response({'status':'error', 'message':'Otp is not valid or expired , kindly request for another pin '}, status=status.HTTP_404_NOT_FOUND )
                else:
                    # deleting the old otp_pin
                    verify.delete()
                    # returning the response
                    return Response({'status':'successful', 'message':'otp is valid'}, status=status.HTTP_201_CREATED )
       
        return Response({'status':'error', 'message':'Otp or email is not valid '}, status=status.HTTP_404_NOT_FOUND )

        

