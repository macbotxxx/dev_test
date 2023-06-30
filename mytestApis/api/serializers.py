from rest_framework import serializers
from django.utils.translation import gettext_lazy as _
from django_filters import rest_framework as filters
from dev_test1.users.models import User  
from mytestApis.models import News


class SendEmailSerializer(serializers.Serializer):
    email = serializers.EmailField( 
        # required = True,
        help_text=_("The primary email address of the user. An Email verification will be required upon successful registration.") 
        )
    
    name = serializers.CharField(
        help_text=_("The name of the user"),
    )

    
    def get_cleaned_data(self):
        return {
            'email': self.validated_data.get('email'),
            'name': self.validated_data.get('name'),
        }
    
    # def validate_email(self, value):
    #     """
    #     Check that the blog post is about Django.
    #     """
    #     if value == "user@example.com":
    #         raise serializers.ValidationError("Blog post is not about Django")
    #     return value
        

class NewsFeedFilter (filters.FilterSet):
    title = filters.CharFilter(field_name="title" , lookup_expr='icontains')
    
    # price = filters.NumberFilter()
    # price__gt = filters.NumberFilter(field_name='price', lookup_expr='gt')
    # price__lt = filters.NumberFilter(field_name='price', lookup_expr='lt')

    # release_year = filters.NumberFilter(field_name='release_date', lookup_expr='year')
    # release_year__gt = filters.NumberFilter(field_name='release_date', lookup_expr='year__gt')
    # release_year__lt = filters.NumberFilter(field_name='release_date', lookup_expr='year__lt')

    # manufacturer__name = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = News
        fields = ['title', 'body',]

class NewsSerializer(serializers.ModelSerializer):

    class Meta:
        model = News
        fields = ['id','title', 'body',]
        read_only_fields = ['id',]


    
   