from django.urls import path
from . import views 

app_name = "otp_section"

urlpatterns = [
    path('send-otp/', views.OtpView.as_view(), name='send-otp'),
    path('verify-otp/<str:email>/<int:otp_pin>/', views.OtpVerificationView.as_view(), name='verify-otp'),
]