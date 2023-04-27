from django.urls import path
from . import views

app_name = "test_feed"

urlpatterns = [
    path('send-email/', views.TestAPIView.as_view(), name = "send_email"),
    path('news-feed/', views.NewsFeedView.as_view(), name = "news-feed"),
    path('news/<int:id>/', views.NewsFeedListView.as_view(), name = "news-action"),
]