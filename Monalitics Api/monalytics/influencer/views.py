from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Influencer
from .serializers import InfluencerSerializer

# Create your views here.


class InfluencerListApiView(APIView):
    """
    this is a class that defines a influencer view
    """

    def post(self, request, *args, **kwargs):
        """
        create a influencer via post method
        """
        data = {
            'full_name': request.data.get('full_name'),
            'email': request.data.get('email'),
            'sector': request.data.get('sector'),
            'social_media': request.data.get('social_media'),
            'password': request.data.get('password')
        }
        list_of_influencers = Influencer.objects.all()
        if list_of_influencers.filter(email=data['email']).exists():
            return Response({'message': 'Influencer already exists with that email'}, status=400)

        serializer = InfluencerSerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def get(self, request, *args, **kwargs):
        """
        to get all influencers
        """
        influencers = Influencer.objects.all()
        serializer = InfluencerSerializer(influencers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        """
        to update a influencer
        """
        influencer = Influencer.objects.get(id=request.data.get('id'))
        serializer = InfluencerSerializer(influencer, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, *args, **kwargs):
        """
        to delete a influencer
        """
        influencer = Influencer.objects.get(id=request.data.get('id'))
        influencer.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def login(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            influencer = Influencer.objects.get(email=email)
        except Influencer.DoesNotExist:
            influencer = None

        if influencer and influencer.authenticate(password):
            # Login successful
            login_status = influencer.logged_in
            influencer = InfluencerSerializer(influencer).data

            return Response({'message': 'Login successful', "influencer": influencer, "login_status": login_status}, status=200)
        else:
            # Invalid credentials
            return Response({'message': 'Invalid credentials'}, status=401)

    def update_login_status(self, request, *args, **kwargs):
        influencer = Influencer.objects.get(id=request.data.get('id'))
        influencer.logged_in = request.data.get('logged_in')
        influencer.save()
        return Response(status=status.HTTP_200_OK)

    def logout(self, request, *args, **kwargs):
        influencer = Influencer.objects.get(id=request.data.get('id'))
        influencer.logged_in = False
        influencer.save()
        return Response(status=status.HTTP_200_OK)
