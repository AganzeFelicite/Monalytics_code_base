
from django.urls import path, include
from .views import (
    CompanyListApiView,
    LoginView
)

urlpatterns = [
    path('api/v1/company/add', CompanyListApiView.as_view()),
    path('api/v1/company/login', LoginView.as_view(), name='login'),
]
