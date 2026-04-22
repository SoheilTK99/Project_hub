from django.shortcuts import render, get_object_or_404
from .models import Portfolio

def portfolio_list(request):
    portfolios = Portfolio.objects.all()
    return render(request, "portfolio/portfolio.html", {"portfolios": portfolios})


def portfolio_detail(request, pk):
    portfolio = get_object_or_404(Portfolio, pk=pk)
    
    # فقط تصاویر غیرخالی
    image_fields = [
        portfolio.image_1, portfolio.image_2, portfolio.image_3, portfolio.image_4,
        portfolio.image_5, portfolio.image_6, portfolio.image_7, portfolio.image_8
    ]
    images = [img for img in image_fields if img]
    
    return render(request, "portfolio/portfolio_detail.html", {
        "portfolio": portfolio,
        "images": images
    })