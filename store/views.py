import json
from django.shortcuts import render, get_object_or_404
from .models import Category, Product
from django.db import connection
from django.urls import reverse

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

    if q:
        query = f"SELECT id, title, price, description, author, in_stock, is_active, image, slug FROM store_product WHERE title LIKE '%{q}%'"

        with connection.cursor() as cursor:
            cursor.execute(query)  
            rows = cursor.fetchall() 
  
        if rows: 
            products = [
                {
                    'id': row[0],
                    'title': row[1],
                    'price': row[2],
                    'description': row[3],
                    'author': row[4],
                    'in_stock': row[5],
                    'is_active': row[6],
                    'image': row[7], 
                    'get_absolute_url': reverse('store:product_detail', args=[row[8]]) 
                } for row in rows
            ]

            searchresult = Searchresult(request)
            searchresult.add(res=json.dumps([p['id'] for p in products]))

            return render(request, 'store/category.html', {
                'products': products,
                'searchresult': f'The search term \"{q}\" found {len(products)} results.'
            })
        else:
            return render(request, 'store/category.html', {
                'products': [],
                'searchresult': f'The search term \"{q}\" found 0 results.'
            })
    else:
        return render(request, 'store/category.html', {
            'searchresult': 'No search term provided.'
        })


""" def search_products(request):  
    q = request.GET.get('q', None)

    if q:
        products = Product.objects.filter(title__icontains=q)

        if products.exists():
            searchresult = Searchresult(request)
            searchresult.add(res=json.dumps(list(products.values('id'))))
            return render(request, 'store/category.html', {
                'products': products,
                'searchresult': f'The search term "{q}" found {len(products)} results.'
            })
        else:
            return render(request, 'store/category.html', {
                'products': {},
                'searchresult': f'The search term "{q}" found 0 results.'
            })
    else:
        return render(request, 'store/category.html', {
            'searchresult': 'No search term provided.'
        }) """

   

