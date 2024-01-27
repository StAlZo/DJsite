"""educational_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from educational_project import settings

from car.views import CarAPIView, CarApi, CarAP

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include('car.urls'))
    path('api/v1/carlist/', CarAPIView.as_view()),
    path('api/v2/carlist/', CarApi.as_view()), #4 vido
    path('api/v3/carlist/<int:pk>/', CarAP.as_view())  #5 video
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)