from django.conf import settings
from django.shortcuts import render
from .models import Service

def service_list(request):
    qs = Service.objects.all()


    return render(request, "service/service.html", {"services": qs})
