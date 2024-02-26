from django.shortcuts import render
from campaign.models import Campaign
from rest_framework import generics
from .serializers import CampaignSerializer
from rest_framework.response import Response
from rest_framework import status


class CompaignListApiView(generics.ListCreateAPIView):
    """
    this is a class that defines a company list api view    
    """
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    queryset = Campaign.objects.all()
    serializer_class = CampaignSerializer

    # 2. Create
    def post(self, request, *args, **kwargs):
        """
        create a company via post method
        """
        data = {
            'title': request.data.get('title'),
            'hash_tag': request.data.get('hash_tag'),
            'time_limit': request.data.get('time_limit'),
            'image_link': request.data.get('image_link'),
            'description': request.data.get('description'),
            # 'influencer': request.data.get('influencer')
        }

        list_of_compaigns = Campaign.objects.all()
        if list_of_compaigns.filter(title=data['title']).exists():
            return Response({'message': 'Campaign already exists with that title'}, status=400)

        serializer = CampaignSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get_remaining_days(self, request, pk):
        """
        Get remaining days for campaign 
        """
        campaign = Campaign.objects.get(id=pk)
        days_left = campaign.get_time_left_in_days()
        return Response({'remaining_days': days_left})
