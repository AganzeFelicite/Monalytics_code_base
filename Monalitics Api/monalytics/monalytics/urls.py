from django.contrib import admin
from django.urls import path, include
from company import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('monalytics-api/', include(urls)),
]
