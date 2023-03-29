from django.urls import path
from . import views 

urlpatterns = [
    path('send-otp/', views.OPT_View.as_view(), name='send-otp'),
    path('verify-otp/<str:email>/<int:otp_pin>/', views.OTP_Verification_View.as_view(), name='verify-otp'),
]