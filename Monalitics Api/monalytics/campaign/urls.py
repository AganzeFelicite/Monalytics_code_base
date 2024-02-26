from django.urls import path, include
from .views import (
    CompaignListApiView,
)

urlpatterns = [
    path('api/v1/company/', CompaignListApiView.as_view(), name='add-campaign'),
]
