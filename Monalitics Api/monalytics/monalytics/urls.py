from django.contrib import admin
from django.urls import path, include
from company import urls
from rest_framework.response import Response


def home(request):
    return Response({'message': 'welcome to monalytics!'})


urlpatterns = [
    path("", home),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('monalytics-api/', include(urls)),
]
