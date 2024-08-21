from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, Product

from django.http import HttpResponse


def all_products(request):
    products= Product.objects.all()
    return render(request, 'store/home.html', {'products':products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product.html', {'product': product})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def categories(request):
    return {
        'categories': Category.objects.all()

    }

