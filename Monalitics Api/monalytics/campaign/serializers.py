from rest_framework import serializers
from .models import Campaign

"""
 serializers here, for the apis jsons
"""


class CampaignSerializer(serializers.ModelSerializer):
    """
    this is a class that defines a campaign serializer
    """
    class Meta:
        model = Campaign
        fields = '__all__'
