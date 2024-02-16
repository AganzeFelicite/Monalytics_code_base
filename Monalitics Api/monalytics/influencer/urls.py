from django.urls import path, include
from .views import (
    InfluencerListApiView,
    InfluencerApiAuthorization
)


urlpatterns = [
    path('api/v1/influencer/login',
         InfluencerApiAuthorization.as_view(), name='login'),
    path('api/v1/influencer/logout',
         InfluencerApiAuthorization.as_view(), name='logout'),
    path('api/v1/influencer/signup',
         InfluencerListApiView.as_view(), name='add-influencer'),
    path('api/v1/influencer/get',
         InfluencerListApiView.as_view(), name='get-influencer'),
    path('api/v1/influencer/update/<int:pk>',
         InfluencerListApiView.as_view(), name='update-influencer'),
    path('api/v1/influencer/delete/<int:pk>',
         InfluencerListApiView.as_view(), name='delete-influencer')
]
