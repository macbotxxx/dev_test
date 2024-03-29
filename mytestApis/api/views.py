# import Django Packages

# import DRF packages
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django_filters import rest_framework as filters
from rest_framework.generics import CreateAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
# import tasks functions
from mytestApis.tasks import send_email_func
# import DRF serializers
from .serializers import SendEmailSerializer , NewsSerializer , NewsFeedFilter
# import app models
from mytestApis.models import News
# from ipware import get_


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
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = NewsFeedFilter

    def get_verisoning(self, request, *args, **kwargs):
        return request.headers.get("Version", None)

    def create (self, request, *args, **kwargs):
        # randomize user email
        email = "user@example.com"
        # email to the given user email address
        send_email_func.delay(email=email)
        # return function response
        return self.create(request, *args, **kwargs)
    
    # def perform_create (self, serializer ):
    #     serializer.save( user = self.request.user )
    

    def get (self, request, *args, **kwargs):
        news_feed = self.get_queryset()
        
        # return function response
        return self.list(request, *args, **kwargs)

    
class NewsFeedListView(RetrieveUpdateDestroyAPIView):
    permission_classes = [ AllowAny, ]
    serializer_class = NewsSerializer
    queryset = News.objects.all()
    lookup_field = 'id'
        