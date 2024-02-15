from django.urls import path, include
from .views import (
    InfluencerListApiView
)

urlpatterns = [
    path('api/v1/influencer/add',
         InfluencerListApiView.as_view().post, name='add-influencer'),
    path('api/v1/influencer/get',
         InfluencerListApiView.as_view().get, name='get-influencer'),
    path('api/v1/influencer/update',
         InfluencerListApiView.as_view().put, name='update-influencer'),
    path('api/v1/influencer/delete',
         InfluencerListApiView.as_view().delete, name='delete-influencer'),

]
