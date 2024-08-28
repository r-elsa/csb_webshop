import json
from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import Category, Product

from django.http import HttpResponse
from django.core.exceptions import ObjectDoesNotExist
from .searchresult import Searchresult

def all_products(request):
    products= Product.objects.all()
    return render(request, 'store/home.html', {'products':products})

def product_detail(request, slug):
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/product.html', {'product': product})

def category_list(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def categories(request):
    return {
        'categories': Category.objects.all()

    }

def search_products(request):  
    q = request.GET.get('q', None)
    
    if q:   
        products = Product.objects.filter(name__icontains=q)
        
        if products.exists():
            product_ids = list(products.values('id'))
            searchresult = Searchresult(request)
            searchresult.add(res=json.dumps(product_ids))
            return render(request, 'store/category.html', {'products': products})
        else:
            return render(request, 'store/category.html', { 'products': {}})
    else:
        # If no query is provided, return the same template with an empty context or a message
        return render(request, 'store/category.html', { 'products': {}})

