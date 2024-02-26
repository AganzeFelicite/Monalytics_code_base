from django.urls import path, include
from .views import (
    CompaignListApiView,
    CampaignRemainingDaysView,
)

urlpatterns = [
    path('api/v1/compaign/', CompaignListApiView.as_view(), name='add-campaign'),
    path('api/v1/compaign/<int:pk>/remaining_days/',
         CampaignRemainingDaysView.as_view(), name='update-campaign'),
]
