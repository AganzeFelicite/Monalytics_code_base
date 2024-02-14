
from django.urls import path, include
from .views import (
    CompanyListApiView,
    LoginView,
    CompanyUpdateApiView,
    SocialMediaAccountApiView,
    CompetitorApiView
)


urlpatterns = [
    path('api/v1/company/add', CompanyListApiView.as_view()),
    path('api/v1/company/login', LoginView.as_view(), name='login'),
    path('api/v1/companies/<int:pk>/',
         CompanyUpdateApiView.as_view(), name='company-update'),
    path('api/v1/companies/social-media/add/<int:company_id>/',
         SocialMediaAccountApiView.as_view(), name='add-social-media'),
    path('api/v1/companies/social-media/delete/<int:social_id>/',
         SocialMediaAccountApiView.as_view(), name='social-media'),
    path('api/v1/companies/competitor/add/<int:company_id>/',
         CompetitorApiView.as_view(), name='get-competitor'),
    path('api/v1/companies/competitor/add/',
         CompetitorApiView.as_view(), name='add-competitor'),

]
