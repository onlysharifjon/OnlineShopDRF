"""
URL configuration for ShopCore project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
# swagger imports

from django.urls import include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# schema view
schema_view = get_schema_view(
    openapi.Info(
        title="ShopCore API",
        default_version='v1',
        description="Test description",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="1234567@gmail.com"), ), )

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('api/user/', include('UserApp.urls')),
    path('api/saler/', include('SalerApp.urls')),
    # path('api/payment/', include('PaymentApp.urls')),
    # path('api/client/', include('ClientApp.urls')),
    # swagger
    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
