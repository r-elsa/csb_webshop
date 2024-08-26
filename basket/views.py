from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .basket import Basket
from store.models import Product

def basket_summary(request):
    basket = Basket(request)
    basket_items = basket.get_items()  # One-liner to get basket items
    return render(request, 'store/basket/summary.html', {'basket_items': basket_items})

def basket_add(request):
    basket = Basket(request)
    if request.POST.get('action') == 'post':
        product_id = int(request.POST.get('product_id'))
        product_qty = int(request.POST.get('product_qty'))
        product = get_object_or_404(Product, id=product_id)
        basket.add(product=product, product_qty=product_qty)
        basket_qty = len(basket)  # Use the __len__ method to get basket quantity
        response = JsonResponse({'qty': basket_qty})
        return response