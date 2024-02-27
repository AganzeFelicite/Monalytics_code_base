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
        read_only_fields = ['id']

    def validate(self, data):
        for field in ['tiktok', 'instagram', 'facebook', 'twitter', 'youtube', 'linkedin', 'snapchat']:
            if field in data:
                data[field] = str(data[field]).lower() == 'true'
        return data
