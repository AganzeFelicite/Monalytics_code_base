from rest_framework import serializers
from .models import Influencer


class InfluencerSerializer(serializers.ModelSerializer):
    """
    this is a class that defines a influencer serializer
    """
    class Meta:
        model = Influencer
        fields = '__all__'
