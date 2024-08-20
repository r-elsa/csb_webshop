from django.shortcuts import render

# Create your views here.
from .models import Category, Product

from django.http import HttpResponse


def all_products(request):
    products= Product.objects.all()
    return render(request, 'store/home.html', {'products':products})


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")

def categories(request):
    return {
        'categories': Category.objects.all()

    }