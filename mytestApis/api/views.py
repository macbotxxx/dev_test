# import Django Packages
from django.core.mail import send_mail
# import DRF packages
from rest_framework.throttling import AnonRateThrottle , UserRateThrottle
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status, serializers
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView , CreateAPIView, UpdateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# import tasks functions
from mytestApis.tasks import send_email_func
# import DRF serializers
from .serializers import SendEmailSerializer , NewsSerializer
# import app models
from mytestApis.models import News



class TestAPIView( CreateAPIView ):
    permission_classes = [ AllowAny, ]
    serializer_class = SendEmailSerializer

    def post( self, request, *args, **kwargs ):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid():
            print(serializer)
            email = serializer.validated_data.get("email")
            # email to the given user email address
            send_email_func.delay(email=email)
            # return function response
            return Response({ 'status':'successful', 'message':'email sent successfully', 'data':serializer.data }, status=status.HTTP_200_OK )
        # return function error response 
        return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST )
    


class NewsFeedView( ListCreateAPIView ):
    permission_classes = [ AllowAny, ]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    throttle_classes = [ UserRateThrottle, ]

    def post (self, request, *args, **kwargs):
        serializer = self.serializer_class( data = request.data )
        if serializer.is_valid():
            serializer.save()
            # randomize user email
            email = "user@example.com"
            # email to the given user email address
            send_email_func.delay(email=email)
            # return function response
            return Response({ 'status':'successful', 'message':'news feed published successfully', 'data':serializer.data }, status=status.HTTP_200_OK )
        
        return Response( serializer.errors , status=status.HTTP_400_BAD_REQUEST )
    

    def get (self, request, *args, **kwargs):
        news_feed = self.get_queryset()
        serializer = self.serializer_class(news_feed , many=True)
        # return function response
        return Response({ 'status':'successful', 'message':'news feed list is fetched successfully', 'data':serializer.data }, status=status.HTTP_200_OK )

    

class NewsFeedListView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ AllowAny, ]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = 'id'
        