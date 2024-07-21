from django.shortcuts import redirect, render
from django.urls import path

from clint import service, views
from clint.models import Clint_management

urlpatterns = [
    path('/create',views.create_somthing, name =""),
     path('store', views.clint_save, name='personal_save'),
    
]