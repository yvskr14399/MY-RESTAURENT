"""shop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',home,name='home'),
    path('menu/',menu,name='menu'),
    path('about/',about,name='about'),
    path('billing/',billing,name='billing'),
    path('records/',records,name='records'),
    path('detailed_monthly_report/',detailed_monthly_report,name='detailed_monthly_report'),
    path('detailed_daily_report/',detailed_daily_report,name='detailed_daily_report'),
    path('detailed_yearly_report/',detailed_yearly_report,name='detailed_yearly_report'),
    path('daily_report/',daily_report,name='daily_report'),
    path('monthly_report/',monthly_report,name='monthly_report'),
    path('yearly_report/',yearly_report,name='yearly_report'),
    path('custom_report/',custom_report,name='custom_report'),
    path('addMenuItem/',addMenuItem,name='addMenuItem'),
  
    
]
