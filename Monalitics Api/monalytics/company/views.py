from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from django.contrib.auth.hashers import make_password
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Company
from .serializers import CompanySerializer


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
        return Response({'message': 'Hello, world!'})

    # 2. Create

    def post(self, request, *args, **kwargs):
        """
        create a company via post method
        """
        data = {
            'company_name': request.data.get('company_name'),
            'email': request.data.get('email'),
            'sector': request.data.get('sector'),
            'password': make_password(request.data.get('password'))
        }
        list_of_companies = Company.objects.all()
        if data['email'] in list_of_companies:
            return Response({'message': 'Company already exists'}, status=400)

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
