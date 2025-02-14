"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include

from config.settings.drf_yasg import schema_view

urlpatterns = [
    #Swagger
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    #Swagger

    #Django Admin urls
    path('api/v1/admin/', admin.site.urls),
    #Django Admin urls

    #Django apps urls
    path('api/v1/users/', include('apps.users.urls')),
    path('api/v1/appeals/', include('apps.appeals.urls')),
    path('api/v1/sponsors/', include('apps.sponsors.urls')),
    path('api/v1/general/', include('apps.general.urls')),
    path('api/v1/authentication/', include('apps.authentication.urls'))
    # Django apps urls

]




