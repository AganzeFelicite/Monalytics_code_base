from django.shortcuts import get_object_or_404
from rest_framework import generics
from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Company, SocialMediaAccount, Competitor
from .serializers import (
    CompanySerializer, SocialMediaAccountSerializer,
    CompetitorSerializer)
"""
these are views for the company app
"""


class CompanyListApiView(APIView):
    """
    this is a class that defines a company list api view    
    """
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    # 1. List all
    def get(self, request, *args, **kwargs):
        """
        to get all companies
        """
        companies = Company.objects.all()
        serializer = CompanySerializer(companies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    # 2. Create

    def post(self, request, *args, **kwargs):
        """
        create a company via post method
        """
        data = {
            'company_name': request.data.get('company_name'),
            'email': request.data.get('email'),
            'sector': request.data.get('sector'),
            'country': request.data.get('country'),
            'city': request.data.get('city'),
            'password': make_password(request.data.get('password'))
        }
        list_of_companies = Company.objects.all()
        if list_of_companies.filter(email=data['email']).exists():
            return Response({'message': 'Company already exists with that email'}, status=400)

        serializer = CompanySerializer(data=data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get('email')
        password = request.data.get('password')
        try:
            company = Company.objects.get(email=email)
        except Company.DoesNotExist:
            company = None

        if company and company.authenticate(password):
            # Login successful
            login_status = company.logged_in
            company = CompanySerializer(company).data

            return Response({'message': 'Login successful', "company": company, "login_status": login_status}, status=200)
        else:
            # Invalid credentials
            return Response({'message': 'Invalid credentials'}, status=401)


class CompanyUpdateApiView(APIView):
    """
    This is a class that defines a company update API view.
    """

    def put(self, request, pk, *args, **kwargs):
        """
        Update a company via PUT method.
        """
        company = get_object_or_404(Company, pk=pk)

        data = {
            'company_name': request.data.get('company_name'),
            'email': request.data.get('email'),
            'sector': request.data.get('sector'),
            'country': request.data.get('country'),
            'city': request.data.get('city'),
        }

        serializer = CompanySerializer(
            instance=company, data=data, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SocialMediaAccountApiView(APIView):
    """
    This is a class that defines a social media account API view.
    """
    # add permission to check if user is authenticated
    # permission_classes = [permissions.IsAuthenticated]

    def post(self, request, company_id, *args, **kwargs):
        """
        Add a social media account to a company.
        """

        company = get_object_or_404(Company, pk=company_id)
        if company.social_media_accounts.filter(account_link=request.data.get('account_link')).exists():
            return Response({'message': 'Social media account already exists'}, status=status.HTTP_400_BAD_REQUEST)

        account = company.addSocialMediaAccount(
            account_link=request.data.get('account_link'),
            social_media_type=request.data.get('social_media_type')
        )
        created_account = SocialMediaAccountSerializer(account)

        return Response({'message': 'Social media account added successfully', 'account': created_account.data,
                         }, status=status.HTTP_201_CREATED)

    def get(self, request, company_id, *args, **kwargs):
        """
        Get all social media accounts.
        """
        socials = SocialMediaAccount.objects.filter(company=company_id)
        serializer = SocialMediaAccountSerializer(socials, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, social_id, *args, **kwargs):
        """
        Delete a social media account.
        """
        social = SocialMediaAccount.objects.get(
            pk=social_id)
        social.delete()
        return Response({'message': 'Social media account deleted successfully'}, status=status.HTTP_200_OK)


class CompetitorApiView(APIView):
    """
    This is a class that defines a competitor API view.
    """

    def get(self, request, *args, company_id, **kwargs):
        """
        get all competitors of a company
        """
        competitors = Competitor.objects.filter(
            company=company_id).values('competitor_name', 'competitor_info', 'id', 'company')
        return Response(competitors, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        """
        Add a competitor to a company.
        """

        company = get_object_or_404(Company, pk=request.data.get('company_id'))
        if company.competitors.filter(competitor_name=request.data.get('competitor_name')).exists():
            return Response({'message': 'Competitor already exists'}, status=status.HTTP_400_BAD_REQUEST)

        competitor = company.addCompetitor(
            competitor_name=request.data.get('competitor_name'),
            competitor_info=request.data.get('competitor_info')
        )
        add_competitor = CompetitorSerializer(competitor)
        return Response({'message': 'Competitor added successfully', 'competitor': add_competitor.data}, status=status.HTTP_201_CREATED)

    def delete(self, request, competitor_id, *args, **kwargs):
        """
        Delete a competitor.
        """
        competitor = Competitor.objects.get(
            pk=competitor_id)
        competitor.delete()
        return Response({'message': 'Competitor deleted successfully'}, status=status.HTTP_200_OK)
