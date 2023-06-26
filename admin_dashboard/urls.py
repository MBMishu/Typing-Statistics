"""cartSite URL Configuration

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
from admin_dashboard import views
urlpatterns = [
    path('', views.index, name="admin_home"),
    path('UserList/', views.UserList, name="UserList"),
    path('details/<str:pk>/', views.details, name="details"),
    path('upload_pdf/', views.upload_pdf, name="upload_pdf"),
    path('upload_pdf/<str:pk>/', views.PdfDelete, name="PdfDelete"),
    path('login/', views.Handlelogin, name="admin_Handlelogin"),
    path('logout/', views.Handlelogout, name="admin_Handlelogout"),
]
