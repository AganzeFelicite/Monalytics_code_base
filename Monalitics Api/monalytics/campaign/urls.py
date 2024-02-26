from django.urls import path, include
from .views import (
    CompaignListApiView,
)

urlpatterns = [
    path('api/v1/compaign/', CompaignListApiView.as_view(), name='add-campaign'),
    path('api/v1/compaign/<int:id>/remaining_days/',
         CompaignListApiView.as_view(), name='update-campaign'),
]
