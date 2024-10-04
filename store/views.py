import json
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
""" from django.utils.html import escape   """

from django.http import HttpResponse
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

    """ # Retrieve the search query from the request and sanitize it.
    q = request.GET.get('q', '').strip()
    
    # Additional validation for input if necessary
    # e.g., restricting the length or pattern of the query
    if len(q) > 100:  # Limit the length of the search query
        return render(request, 'store/category.html', {
            'products': {},
            'searchresult': 'Search term too long. Please use a shorter term.'
        }) """
    
    if q:

        """ # Using parameterized query
        products = Product.objects.filter(title__icontains=q) """
        products = Product.objects.filter(title=q)

       
        
        
        if products.exists():
            product_ids = list(products.values('id'))
            searchresult = Searchresult(request)
            searchresult.add(res=json.dumps(product_ids))
            """ # Use escape to safely render the query in the template context
            escaped_q = escape(q) """
            return render(request, 'store/category.html', {'products': products, 'searchresult': f'The search term "{q}" found {len(products)} results.'})
        else:
            return render(request, 'store/category.html', { 'products': {},  'searchresult': f'The search term "{q}" found {len(products)} results.'})

    else:
        return render(request, 'store/category.html', {  'searchresult': f'The search term " " found 0 results.'})

