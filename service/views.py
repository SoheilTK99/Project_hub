from django.shortcuts import render
from .import Service

def service_list(request):
    service_list = Service.objects.all(),
    context = {
        'services : service_list'
    }
    return render(request,"service/service.html",context)