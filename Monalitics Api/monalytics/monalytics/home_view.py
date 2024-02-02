from rest_framework.response import Response


def home():
    return Response({'message': 'welcome to monalytics!'})
