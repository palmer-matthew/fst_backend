"""fst_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.conf.urls import url, include
from core.views import TestView
from core.views import ContactView
from core.views import ScholarshipView

urlpatterns = [
    url(r'^api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('testview/', TestView.as_view()),
    path('contact/', ContactView.as_view()),
    path('scholarship/', ScholarshipView.as_view()),
]
