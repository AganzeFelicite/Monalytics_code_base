from rest_framework import serializers
from .models import Company, SocialMediaAccount, Competitor

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


class CompetitorSerializer(serializers.ModelSerializer):
    """
    this is a class that defines a competitor serializer
    """
    class Meta:
        model = Competitor
        fields = '__all__'
