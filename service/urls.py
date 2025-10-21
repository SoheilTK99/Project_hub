from django.urls import path
from django.views.generic import TemplateView
from .import views


urlspatterns = [
    path('', views.service_list, name='service')
    
]


