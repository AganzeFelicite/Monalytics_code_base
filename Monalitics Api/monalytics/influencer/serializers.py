from rest_framework import serializers
from .models import Influencer
from campaign.serializers import CampaignSerializer


class InfluencerSerializer(serializers.ModelSerializer):
    """
    this is a class that defines a influencer serializer
    """
    campaigns = CampaignSerializer(many=True, read_only=True)

    class Meta:
        model = Influencer
        fields = '__all__'
        read_only_fields = ['id']

    def get_campaigns(self, influencer):
        return CampaignSerializer(influencer.get_campaigns(), many=True).data
