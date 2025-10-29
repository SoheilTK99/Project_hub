from django.urls import path
from .import views

app_name = 'service'

urlpatterns = [
    path('', views.service_list, name='list'),
    path('<int:pk>/', views.service_detail, name='detail'),
    
]


