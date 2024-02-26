from django.contrib import admin
from django.urls import path, include
from company import urls
from rest_framework.response import Response

from rest_framework.views import APIView


class HomeView(APIView):
    def get(self, request):
        data = {'message': 'Welcome to Monalytics!'}
        return Response(data)


urlpatterns = [
    path("", HomeView.as_view()),
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('monalytics-api/', include(urls)),
    path('influencer/', include('influencer.urls')),
    path('campaign/', include('campaign.urls')),
]
