from django.urls import path, include
from .views import (
    InfluencerListApiView
)


urlpatterns = [
    path('api/v1/influencer/login', InfluencerListApiView.as_view(), name='login'),
    path('api/v1/influencer/logout',
         InfluencerListApiView.as_view(), name='logout'),
    path('api/v1/influencer/signup',
         InfluencerListApiView.as_view(), name='add-influencer'),
    path('api/v1/influencer/get',
         InfluencerListApiView.as_view(), name='get-influencer'),
    path('api/v1/influencer/update',
         InfluencerListApiView.as_view(), name='update-influencer'),
    path('api/v1/influencer/delete',
         InfluencerListApiView.as_view(), name='delete-influencer')
]
