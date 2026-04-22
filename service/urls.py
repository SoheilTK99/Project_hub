# service/urls.py
from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('webdesign/', TemplateView.as_view(template_name='service/webdesign.html'), name='webdesign'),
    path('seo/', TemplateView.as_view(template_name='service/seo.html'), name='seo'),
]
