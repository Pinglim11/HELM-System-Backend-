"""onesimus URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path 
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('employeeform', views.employeeform, name = 'employeeform'),
    path('createrecord', views.createrecord, name = 'createrecord'),
    path('test', views.testing, name='test'),
    path('viewtest', views.viewtest, name='viewtest'),
    path('logout', views.logoutuser, name='logout'),
    path('employee/<int:empid>/', views.employeeprof, name='record'),
    path('employee/<int:empid>/edit', views.employeeedit, name='edit'),
    path('employee/<int:empid>/delete', views.employeedelete, name='delete'),
    path('viewtest_awards', views.viewtest_awards, name='viewtest_awards'),
] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

