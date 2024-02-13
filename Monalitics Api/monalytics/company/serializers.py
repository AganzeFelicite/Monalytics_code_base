from rest_framework import serializers
from .models import Company, SocialMediaAccount

"""
 serializers here, for the apis jsons
"""


class CompanySerializer(serializers.ModelSerializer):
    """
    this is a class that defines a company serializer
    """
    class Meta:
        model = Company
        fields = '__all__'


class SocialMediaAccountSerializer(serializers.ModelSerializer):
    """
    this is a class that defines a social media account serializer
    """
    class Meta:
        model = SocialMediaAccount
        fields = '__all__'
