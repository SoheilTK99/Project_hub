from django.shortcuts import render, get_object_or_404
from .models import Service

def service_list(request):
    services = Service.objects.all()
    return render(request, "service/service.html", {"services": services})


def service_detail(request, pk):
    service = get_object_or_404(Service, pk=pk)
    
    # فقط تصاویر غیرخالی
    image_fields = [
        service.image_1, service.image_2, service.image_3, service.image_4,
        service.image_5, service.image_6, service.image_7, service.image_8
    ]
    images = [img for img in image_fields if img]
    
    return render(request, "service/service_detail.html", {
        "service": service,
        "images": images
    })