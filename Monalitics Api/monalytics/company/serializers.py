from rest_framework import serializers
from .models import Company

"""
 serializers here, for the apis jsons
"""


class CompanySerializer(serializers.ModelSerializer):
    """
    this is a class that defines a company serializer
    """
    class Meta:
        model = Company
        fields = ['id', 'company_name', 'email',
                  'sector', 'password']
