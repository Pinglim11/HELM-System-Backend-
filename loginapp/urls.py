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
    path('', views.home, name = 'home'),
    path('employeeform', views.employeeform, name = 'employeeform'),
    path('createrecord', views.createrecord, name = 'createrecord'),
    path('test', views.testing, name='test'),
    #path('viewtest', views.viewtest, name='viewtest'),
    path('logout', views.logoutuser, name='logout'),
    path('genreport', views.genreport, name='genreport'),
    path('employee/<int:empid>/', views.employeeprof, name='record'),
    path('download/<int:did>/', views.download, name='download'),
    path('document/<int:did>/', views.document, name='document'),
    path('document/<int:did>/delete', views.documentsdelete, name='documentsdelete'),
    path('employee/<int:empid>/editdocument/<int:did>/', views.editedocument, name='editedocument'),
    path('employee/<int:empid>/editrecord', views.editrecord, name='editrecord'),
    path('employee/<int:empid>/editpersonal', views.editpersonal, name='editpersonal'),
    path('employee/<int:empid>/editemergency', views.editemergency, name='editemergency'),
    path('employee/<int:empid>/editemphistory', views.editemphistory, name='editemphistory'),
    path('employee/<int:empid>/editeducation', views.editeducation, name='editeducation'),
    path('employee/<int:empid>/editfamily', views.editfamily, name='editfamily'),
    path('employee/<int:empid>/editspouse', views.editspouse, name='editspouse'),
    path('employee/<int:empid>/editchild', views.editchild, name='editchild'),
    path('employee/<int:empid>/editone', views.editone, name='editone'),
    path('employee/<int:empid>/delete', views.employeedelete, name='delete'),
    path('employee/<int:empid>/upload', views.uploademployeerecord, name='upload'),
    path('awards/<int:did>/', views.awardsprofile, name='awardsprofile'),
    path('awards/<int:did>/editdocument', views.editadocument, name='editadocument'),
    path('awards/<int:did>/editrecord', views.editawardrecord, name='editawardrecord'),
    path('discipline/<int:did>/', views.disciplineprofile, name='disciplineprofile'),
    path('discipline/<int:did>/editdocument', views.editddocument, name='editddocument'),
    path('discipline/<int:did>/editrecord', views.editdisciplinerecord, name='editdisciplinerecord'),
    path('viewtest_awards', views.viewtest_awards, name='viewtest_awards'),
    path('uploadaward', views.uploadaward, name='uploadaward'),
    path('uploaddiscipline', views.uploaddiscipline, name='uploaddiscipline'),
    path('viewtest_discipline', views.viewtest_discipline, name='viewtest_discipline'),
    path('viewreport', views.viewreport, name='viewreport'),
    path('viewtest_home', views.home, name='viewtest_home'),
    path('markasread', views.markasread, name='markasread'),


] +  static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)# + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

